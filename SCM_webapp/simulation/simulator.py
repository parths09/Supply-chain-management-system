from datetime import timedelta
from datetime import datetime
from django.utils.timezone import now
from .models import Shipment,Procurement,Order
from .utils import *
from .query import *
from .insertion_data import orders_data

def get_difference(date1,date2):
    date1=datetime.date(date1)
    # Define two dates in YYYY-MM-DD format
    # date1 = datetime.strptime(date1, "%Y-%m-%d")
    # date2 = datetime.strptime(date2, "%Y-%m-%d")

    # Get the difference
    difference = date1 - date2

    # Output in days
    # print(f"Difference: {difference.days} days")
    return int(difference.days)


def simulate_one_day(current_day:str,seek):
    current_day_str = current_day
    current_day=datetime.fromisoformat(current_day)
    seek=int(seek)
    print(seek)

    log_messages = []

    #Make changes with respect to current day

    #Insertions
    # fetch line for insertion from a file (for current day only, say take 5 fetches)
    # this fetch contains insertions for orders,order_details,shippings
    # estimate delivery date for each shipment. shipping_status = pending/processing
    # insert into orders, shippings,order_details

    # Create script and fetch them
    # Create query functions to insert
    # Insert
    if seek<len(orders_data):
        order=orders_data[seek]

        order_date = current_day_str
        # print("order_date",order_date)
        add_order(order["order_id"],order['customer_id'],order_date,order["total_amount"],order["status"])
        log_messages.append(f"Inserted order {order['order_id']} for customer {order['customer_id']}.")

        for ship in order["shippings"]:
            w_id = get_warehouse_id(ship['items'][0]['inventory_id'])
            cost,steps=dijkstra(graph,f'W{w_id}',f'C{order['customer_id']}')
            total_cost = cost+len(steps)
            delivery_date = current_day+timedelta(days=total_cost)
            delivery_date=datetime.strftime(delivery_date,"%Y-%m-%d")
            # print("Delivery date",delivery_date)
            add_shipping(ship["shipping_id"],delivery_date,ship["tracking_number"],ship["status"],order_date)
            log_messages.append(f"Inserted shipping {ship['shipping_id']} with delivery date {delivery_date} for order {order['order_id']}.")

            for item in ship["items"]:
                add_order_details(order['order_id'],item["inventory_id"],ship['shipping_id'],item["quantity"],item["amount"])
                log_messages.append(f"Inserted order detail: innventory {item['inventory_id']} (qty: {item['quantity']}) in shipping {ship['shipping_id']}.")


    #Updations
    # Go through shippings table to see status. If not delivered, potential update
    # if status is pending/processing update it to shipped and add entry into shipping_details
    # if status is shipped then update status to next status {in transit,out for delivery} depending upon next_warehouse column in shipping_details
    # if status is in transit compute difference in current_date and last_updated in shippings and compare it with days required to go to next warehouse. If equal, update status to shipped and last_updated. Add entry into shipping_details.
    # if status if out for delivery change it to delivered and update last_updated.
    
    for shipment in Shipment.objects.filter():
        # print(shipment.delivery_date,shipment.shipping_id,shipment.tracking_number)
        if shipment.shipping_status=='Processing' or shipment.shipping_status == 'Pending':
            # update shipping_status to shipped, last_updated = current_day. Make entry into shipping_details
            shipment.shipping_status='Shipped'
            shipment.last_updated=current_day_str
            log_messages.append(f"Updated shipment {shipment.shipping_id} status to {shipment.shipping_status}.")

            current_warehouse=get_source(shipment.shipping_id)
            dest=get_destination(shipment.shipping_id)
            next_warehouse,cost=get_next_position(f'W{current_warehouse}',dest)
            next_warehouse=int(next_warehouse[1:]) if next_warehouse[0]!='C' else None

            add_shipping_detail(shipment.shipping_id,current_day_str,current_warehouse,next_warehouse)

        elif shipment.shipping_status=='In Transit':
            # get current position from shipping_details using query
            # if get_next_position(current_position) cost is equal to current_day - last_updated then update to Shipped.
            # Also make entry into shipping_details using query.
            current_warehouse=get_current_position(shipment.shipping_id)
            # print("Shipping id :",shipment.shipping_id,"CurrWarehouse",current_warehouse)
            dest=get_destination(shipment.shipping_id)
            next_warehouse,cost=get_next_position(f'W{current_warehouse}',dest)

            if cost==get_difference(current_day,shipment.last_updated):
                upcoming_warehouse,_=get_next_position(next_warehouse,dest)
                upcoming_warehouse=int(upcoming_warehouse[1:]) if upcoming_warehouse[0]!='C' else None
                add_shipping_detail(shipment.shipping_id,current_day,int(next_warehouse[1:]),upcoming_warehouse)
                shipment.shipping_status="Shipped"
                shipment.last_updated=current_day_str
                log_messages.append(f"Updated shipment {shipment.shipping_id} status to {shipment.shipping_status}.")
            
        elif shipment.shipping_status=='Shipped':
            # update shipping_status to In Transit/Out for Delivery, last_updated = current_day
            # get current position from shipping_details using query
            # if get_next_position(current_position) starts with C, status = Out for Delivery else In Transit
            current_warehouse=get_current_position(shipment.shipping_id)
            dest=get_destination(shipment.shipping_id)
            next_warehouse,cost=get_next_position(f'W{current_warehouse}',dest)
            if next_warehouse[0]!='C':
                shipment.shipping_status='In Transit'
                shipment.last_updated=current_day_str
            else:
                shipment.shipping_status='Out for Delivery'
                shipment.last_updated=current_day_str
            log_messages.append(f"Updated shipment {shipment.shipping_id} status to {shipment.shipping_status}.")
                
        elif shipment.shipping_status=='Out for Delivery':
            # update shipping_status to Delivered and last_updated = current_date
            shipment.shipping_status='Delivered'
            shipment.last_updated=current_day_str
            shipment.save()
            log_messages.append(f"Updated shipment {shipment.shipping_id} status to {shipment.shipping_status}.")
        if shipment.shipping_status!='Delivered':
            shipment.save()



    # Go through procurements table checking status. If not delivered, potential update
    # If status is processing change it to in transit and update last updated
    # If status is in transit check delivery_date = current_day then change status to delivered and exit.
    for p in Procurement.objects.filter():
        if p.status=="Processing":
            p.status='In transit'
            p.last_updated=current_day_str
            p.save()
            log_messages.append(f"Procurement {p.procurement_id} status updated to {p.status}.")
        elif p.status=='In transit':
            if current_day_str==datetime.strftime(p.delivery_date,"%Y-%m-%d"): # it can be done using graphs too
                p.status='Delivered'
                p.last_updated=current_day_str
                log_messages.append(f"Procurement {p.procurement_id} status updated to {p.status}.")
                p.save()

    # Go through orders table, check if all of its shipments are delivered
    for order in Order.objects.filter():
        if order.order_status=='Pending' or order.order_status=='Confirmed':
            order.order_status='On the way'
            order.save()
            log_messages.append(f"Order {order.order_id} status updated to {order.order_status}.")
        check=check_order_completed(order.order_id)
        if check is True:
            order.order_status='Completed'
            order.save()
            log_messages.append(f"Order {order.order_id} status updated to {order.order_status}.")


    #increment the day and return it
    #maybe keep log of all changes made and return it too
    next_day = current_day+timedelta(days=1)
    return datetime.strftime(next_day,"%Y-%m-%d"),seek+1,log_messages

def get_current_date():
    import os

    # Build the path relative to the current file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'date.txt')

    try:
        with open(file_path, 'r') as file:
            date_str = file.read().strip()
            return date_str
    except FileNotFoundError:
        return "date.txt not found"
    except Exception as e:
        return f"Error reading date.txt: {e}"