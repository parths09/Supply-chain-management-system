from django.shortcuts import render, redirect
from customer.query import *
from django.contrib import messages

# Create your views here.
def customer_home(request):
    return render(request, 'customer_home.html', {'username': request.user.username})


def customer_orders(request):
    dict_1={
        'pending': 'pending',
        'processing': 'pending',
        'shipped': 'arriving',
        'in transit': 'arriving',
        'out for delivery': 'out for delivery',
        'delivered': 'delivered',
        'cancelled': 'cancelled',
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
        if status in ('shipped', 'in transit'):
            order['status'] = 'arriving'
        elif status in ('pending', 'processing'):
            order['status'] = 'pending'

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
    return render(request, "customer_tracking.html", {"tracking_number": tracking_number})
