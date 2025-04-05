from django.shortcuts import render, redirect
from customer.query import *
from django.contrib import messages

# Create your views here.
def customer_home(request):
    return render(request, 'customer_home.html', {'username': request.user.username})


def customer_orders(request):
    
    all_orders = cus_orders(name=request.user.username)
    print(all_orders)
    filtered_orders = all_orders  # initially keep all
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
            dict={
                'pending': ('pending'),
                'delivered': ('completed'),
                'on the way': ('on the way' , 'confirmed')
            }
            status=dict.get(status_filter)
            filtered_orders = [order for order in all_orders if order.get('status') in status]

    context = {
            "username": request.user.username,
            "orders": filtered_orders,
            }

    return render(request, "customer_order.html", context)




def tracking_page(request, tracking_number):
    return render(request, "customer_tracking.html", {"tracking_number": tracking_number})
