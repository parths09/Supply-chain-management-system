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
        w_id=get_warehouse_id(request.user.username)
        w_name = get_warehouse_name(w_id)
        result = get_active_shipments(w_id)
        active_shipments = []
        for row in result:
            shipments_dict = {}
            shipments_dict['shipping_id'] = row.shp_id
            shipments_dict['tracking_number'] = row.tracking_number
            shipments_dict['move_to'] = get_warehouse_name(row.move_to) if row.move_to else 'Delivery location'
            shipments_dict['shipping_status'] = row.shipping_status
            shipments_dict['delivery_date'] = row.delivery_date
            active_shipments.append(shipments_dict)
        context = {
            'username': request.user.username,
            'active_shipments':active_shipments,
            'warehouse_name':w_name,
        }
        return render(request,'manager_shipments.html',context)

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
        w_id=get_warehouse_id(request.user.username)
        w_name = get_warehouse_name(w_id)
        employees = get_employees(w_id)

        context = {
            'username': request.user.username,
            'employees': employees,
            'warehouse_name':w_name,
        }
        return render(request,'manager_employees.html',context)

def manager_procurements(request):
    if request.method=='POST':
        return render(request,'manager_procurements.html',{'username': request.user.username})
    else:
        return render(request,'manager_procurements.html',{'username': request.user.username})