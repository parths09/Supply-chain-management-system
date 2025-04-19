from datetime import timedelta
from datetime import datetime
from django.utils.timezone import now
from .models import Shipment,Procurement
from .utils import *
from .query import *

def simulate_one_day(current_day:str):
    current_day=datetime.fromisoformat(current_day)
    #Make changes with respect to current day

    #Insertions
    # fetch line for insertion from a file (for current day only, say take 5 fetches)
    # this fetch contains insertions for orders,order_details,shippings
    # estimate delivery date for each shipment. shipping_status = pending/processing
    # insert into orders, shippings,order_details

    # Create script and fetch them
    # Create query functions to insert
    # Insert


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
            shipment.last_updated=current_day
            current_warehouse=get_source(shipment.shipping_id)
            dest=get_destination(shipment.shipping_id)
            next_warehouse,cost=get_next_position(f'W{current_warehouse}',dest)
            next_warehouse=int(next_warehouse[1:]) if next_warehouse[0]!='C' else None
            # add_shipping_detail(shipment.shipping_id,current_day,current_warehouse,next_warehouse)

        elif shipment.shipping_status=='In Transit':
            # get current position from shipping_details using query
            # if get_next_position(current_position) cost is equal to current_day - last_updated then update to Shipped.
            # Also make entry into shipping_details using query.
            current_warehouse=get_current_position(shipment.shipping_id)
            dest=get_destination(shipment.shipping_id)
            next_warehouse,cost=get_next_position(f'W{current_warehouse}',dest)
            # if cost==(current_day-shipment.last_updated):
            #     next_warehouse=int(next_warehouse[1:]) if next_warehouse[0]!='C' else None
            #     # add_shipping_detail(shipment.shipping_id,current_day,current_warehouse,next_warehouse)
            #     shipment.shipping_status="Shipped"
            #     shipment.last_updated=current_day
            
        elif shipment.shipping_status=='Shipped':
            # update shipping_status to In Transit/Out for Delivery, last_updated = current_day
            # get current position from shipping_details using query
            # if get_next_position(current_position) starts with C, status = Out for Delivery else In Transit
            current_warehouse=get_current_position(shipment.shipping_id)
            dest=get_destination(shipment.shipping_id)
            next_warehouse,cost=get_next_position(f'W{current_warehouse}',dest)
            if next_warehouse[0]!='C':
                shipment.shipping_status='In Transit'
                shipment.last_updated=current_day
            else:
                shipment.shipping_status='Out for Delivery'
                shipment.last_updated=current_day
                
        elif shipment.shipping_status=='Out for Delivery':
            # update shipping_status to Delivered and last_updated = current_date
            shipment.shipping_status='Delivered'
            shipment.last_updated=current_day



    # Go through procurements table checking status. If not delivered, potential update
    # If status is processing change it to in transit and update last updated
    # If status is in transit check delivery_date = current_day then change status to delivered and exit.
    for p in Procurement.objects.filter():
        # print("proc",p.procurement_id)
        if p.status=="Processing":
            p.status='In Transit'
            p.last_updated=current_day
        elif p.status=='In Transit':
            if current_day==p.delivery_date: # it can be done using graphs too
                p.status='Delivered'
                p.last_updated=current_day



    #increment the day and return it
    #maybe keep log of all changes made and return it too
    next_day = current_day+timedelta(days=1)
    next_day.isoformat()
    return next_day.isoformat()

