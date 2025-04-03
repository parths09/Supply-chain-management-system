from django.shortcuts import render

# Create your views here.
def customer_home(request):
    if request.method=='POST':
        return render(request,'customer_home.html',{'username': request.user.username})
    else:
        return render(request,'customer_home.html',{'username': request.user.username})
    

def customer_shipments(request):
    # Example data (replace with real data from DB)
    shipments = [
        {"tracking_number": "123456", "status": "In Transit", "delivery_date": "2025-04-05", "origin": "New York", "destination": "Los Angeles"},
        {"tracking_number": "789012", "status": "Delivered", "delivery_date": "2025-03-30", "origin": "Chicago", "destination": "Houston"},
    ]
    
    context = {
        "username": request.user.username ,
        "shipments": shipments
    }
    
    return render(request, "customer_shipment.html", context)
