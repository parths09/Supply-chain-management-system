from django.shortcuts import render,redirect
from customer.query import *
from django.contrib import messages

# Create your views here.
def customer_home(request):
    if request.method=='POST':
        return render(request,'customer_home.html',{'username': request.user.username})
    else:
        return render(request,'customer_home.html',{'username': request.user.username})
    

def customer_shipments(request):

    shipments = cus_shipments(request.user.username)

    if request.method == 'GET' and 'tracking_number' in request.GET:
        tracking_number = request.GET.get('tracking_number')
        tracking_numbers = [shipment['tracking_number'] for shipment in shipments]
        if tracking_number in tracking_numbers:
            return redirect('tracking_page', tracking_number=tracking_number)
        else:
            messages.error(request, "Invalid Tracking Number.")
            return redirect('customer_shipments')

    
    context = {
        "username": request.user.username,
        "shipments": shipments
    }
    return render(request, "customer_shipment.html", context)


def tracking_page(request, tracking_number):
    return render(request, "customer_tracking.html", {"tracking_number": tracking_number})