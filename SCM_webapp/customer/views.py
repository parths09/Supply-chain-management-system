from django.shortcuts import render, redirect
from customer.query import *
from django.contrib import messages

# Create your views here.
def customer_home(request):
    return render(request, 'customer_home.html', {'username': request.user.username})


def customer_orders(request):
    all_orders = cus_orders(name=request.user.username)
    filtered_orders = all_orders  # initially keep all
    
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
    if status_filter:
        filtered_orders = [order for order in all_orders if order.get('status') == status_filter]

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
    # print(shipping_stautus)
    order_date=cus_order_date(tracking_number)
    delivery=cus_expected_delivery(tracking_number)
    progress_unit = len(tracking_details)-1
    # print(order_date)
    # print(delivery)
    print(progress_unit)
    fill_circle = False
    if shipping_status == 'shipped':
        progress_height = 90 + 110*progress_unit
        fill_circle = True
    elif shipping_status == 'processing':
        progress_height = 45
    elif shipping_status == 'delivered':
        progress_height = 90 + 110*progress_unit+110
    else:
        progress_height = 90 + 110*progress_unit + 55



    

    context = {
        "tracking_number": tracking_number,
        "tracking_details":tracking_details,
        "shipping_status" : shipping_status,
        "order_date" : order_date   ,
        "expected_delivery" : delivery,
        "progress_height" : progress_height,
        "fill_circle" : fill_circle
        }
    return render(request, "customer_tracking.html",context )
