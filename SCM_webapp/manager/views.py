from django.shortcuts import render
from manager.query import *

# Create your views here.

def manager_home(request):
    if request.method=='POST':
        return render(request,'manager_home.html',{'username': request.user.username})
    else:
        return render(request,'manager_home.html',{'username': request.user.username})
     

def manager_shipments(request):
    if request.method=='POST':
        return render(request,'manager_shipments.html',{'username': request.user.username})
    else:
        return render(request,'manager_shipments.html',{'username': request.user.username})

def manager_stocks(request):
    if request.method=='POST':
        return render(request,'manager_stocks.html',{'username': request.user.username})
    else:
        w_id=get_warehouse_id(request.user.username)
        warehouse_products=get_warehouse_products(w_id)
        context = {
            'username': request.user.username,
            "warehouse_products":warehouse_products,
        }
        print(warehouse_products)
        return render(request,'manager_stocks.html',context)

def manager_employees(request):
    if request.method=='POST':
        return render(request,'manager_employees.html',{'username': request.user.username})
    else:
        return render(request,'manager_employees.html',{'username': request.user.username})

def manager_procurements(request):
    if request.method=='POST':
        return render(request,'manager_procurements.html',{'username': request.user.username})
    else:
        return render(request,'manager_procurements.html',{'username': request.user.username})