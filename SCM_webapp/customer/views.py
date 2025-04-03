from django.shortcuts import render
from customer.query import *

# Create your views here.
def customer_home(request):
    if request.method=='POST':
        return render(request,'customer_home.html',{'username': request.user.username})
    else:
        return render(request,'customer_home.html',{'username': request.user.username})
    

def customer_shipments(request):
    # Example data (replace with real data from DB)
    shipments = cus_shipments(request.user.username)
    
    context = {
        "username": request.user.username ,
        "shipments": shipments
    }
    
    return render(request, "customer_shipment.html", context)
