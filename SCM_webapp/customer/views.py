from django.shortcuts import render, redirect
from customer.query import *
from django.contrib import messages

# Create your views here.
def customer_home(request):
    return render(request, 'customer_home.html', {'username': request.user.username})


def customer_orders(request):
    dict_1={
        'Pending': 'Pending',
        'Processing': 'Pending',
        'Shipped': 'Arriving',
        'In Transit': 'Arriving',
        'Out for Delivery': 'Out for delivery',
        'Delivered': 'Delivered',
        'Cancelled': 'Cancelled',
    }
                
    dict_2={
            'pending': ('pending','processing'),
            'arriving': ('shipped','in transit'),
            'out for delivery': ('out for delivery'),
            'delivered': ('delivered'),
            'cancelled': ('cancelled'),

            }
    

    all_orders = cus_orders(name=request.user.username)
    filtered_orders = all_orders 
    for i in range(len(filtered_orders)):
        order = dict(filtered_orders[i]) 
        status = order.get('status')
        order['status'] = dict_1.get(status)
        filtered_orders[i] = order 

    if request.method == 'GET':

        tracking_number = request.GET.get('tracking_number', '').strip()
        status_filter = request.GET.get('status', '').strip()

        if tracking_number:

            tracking_numbers = [order['tracking_number'] for order in all_orders]

            if tracking_number in tracking_numbers:
                return redirect('tracking_page', tracking_number=tracking_number)
            else:
                messages.error(request, "Invalid Tracking Number.")
                return redirect('customer_orders')


        # If status filter is provided — filter
        if status_filter and status_filter != 'all':
            #status=('pending', 'confirmed', 'completed', 'on the way')

            filtered_orders = [order for order in filtered_orders if order.get('status')==status_filter]

    context = {
            "username": request.user.username,
            "orders": filtered_orders,
            }

    return render(request, "customer_order.html", context)




def tracking_page(request, tracking_number):
    tracking_details=cus_tracking(tracking_number)
    # print(tracking_details)
    # if tracking_details[-1]["move_to"] is None:
    #     tracking_details[-1]["move_to"] = "Delivering"
    shipping_status = cus_shipping_status(tracking_number)[0]
    # order_date=cus_order_date(tracking_number)
    # delivery=cus_expected_delivery(tracking_number)
    
    progress_unit = len(tracking_details)-1
    fill_circle = False
    if shipping_status == 'Shipped':
        progress_height = 6  + 6.5*progress_unit
        fill_circle = True
    elif shipping_status == 'Processing':
        progress_height = 3
    elif shipping_status == 'Delivered':
        progress_height = 6 + 6.5*progress_unit+6
    else:
        progress_height = 6 + 6.5*progress_unit + 4

    product_details = cus_product_details(tracking_number)


    context = {
        "tracking_number": tracking_number,
        "tracking_details":tracking_details,
        "progress_height" : progress_height,
        "fill_circle" : fill_circle,
        "product_details":product_details,
        "username": request.user.username
        }
    return render(request, "customer_tracking.html",context )
