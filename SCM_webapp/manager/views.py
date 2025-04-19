from django.shortcuts import render,redirect
from manager.query import *
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.

def manager_home(request):
    if request.method=='POST':
        return render(request,'manager_home.html',{'username': request.user.username})
    else:
        w_id = get_warehouse_id(request.user.username)
        low_stocks= get_low_stock(w_id)
        incoming_procurements=get_incoming_procurements(w_id)
        notifications = get_manager_notifications(w_id)
        notifications_unread = False
        for note in notifications:
            if note['is_read']==False:
                notifications_unread=True
                break
        context = {
            'username': request.user.username,
            'low_stocks':low_stocks,
            'warehouse_name':get_warehouse_name(w_id),
            'incoming_procurements':incoming_procurements,
            'notifications':notifications,
            'notifications_unread':notifications_unread,
        }
        return render(request,'manager_home.html',context)
     

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
        notifications = get_manager_notifications(w_id)
        notifications_unread = False
        for note in notifications:
            if note['is_read']==False:
                notifications_unread=True
                break
        context = {
            'username': request.user.username,
            'active_shipments':active_shipments,
            'warehouse_name':w_name,
            'notifications':notifications,
            'notifications_unread':notifications_unread,
        }
        return render(request,'manager_shipments.html',context)

def manager_stocks(request):
    if request.method=='POST':
        return render(request,'manager_stocks.html',{'username': request.user.username})
    else:
        w_id=get_warehouse_id(request.user.username)
        warehouse_products=get_warehouse_products(w_id)
        notifications = get_manager_notifications(w_id)
        notifications_unread = False
        for note in notifications:
            if note['is_read']==False:
                notifications_unread=True
                break
        context = {
            'username': request.user.username,
            "warehouse_products":warehouse_products,
            'notifications':notifications,
            'notifications_unread':notifications_unread
        }
        return render(request,'manager_stocks.html',context)

def manager_employees(request):
    if request.method=='POST':
        return render(request,'manager_employees.html',{'username': request.user.username})
    else:
        w_id=get_warehouse_id(request.user.username)
        w_name = get_warehouse_name(w_id)
        employees = get_employees(w_id)
        notifications = get_manager_notifications(w_id)
        notifications_unread = False
        for note in notifications:
            if note['is_read']==False:
                notifications_unread=True
                break
        context = {
            'username': request.user.username,
            'employees': employees,
            'warehouse_name':w_name,
            'notifications':notifications,
            'notifications_unread':notifications_unread
        }
        return render(request,'manager_employees.html',context)

def manager_procurements(request):
    if request.method=='POST':
        return render(request,'manager_procurements.html',{'username': request.user.username})
    else:
        w_id = get_warehouse_id(request.user.username)
        product_details = get_products()
        notifications = get_manager_notifications(w_id)
        notifications_unread = False
        for note in notifications:
            if note['is_read']==False:
                notifications_unread=True
                break
        context = {
            'products':product_details,
            'username':request.user.username,
            'notifications':notifications,
            'notifications_unread':notifications_unread
        }
        return render(request,'manager_procurements.html',context)
    

def ignore_alert(request,inventory_id):
    if request.method=='POST':
        update_ignore_alert(inventory_id)
        return redirect('/manager')
    else:
        return render(request,'manager_procurements.html',{'username': request.user.username})
    
def get_suppliers(request):
    product_id = request.GET.get('product_id')
    suppliers_data = get_filtered_suppliers(product_id)
    data = [dict(row) for row in suppliers_data]  # Convert each RowMapping to dict
    return JsonResponse(data,safe=False)

def get_price(request):
    product_id = request.GET.get('product_id')
    supplier_id = request.GET.get('supplier_id')
    price = get_price_detail(product_id,supplier_id)
    return JsonResponse({'unit_price': price})

def check_inventory(request):
    product_id = request.GET.get("product_id")
    supplier_id = request.GET.get("supplier_id")
    w_id=get_warehouse_id(request.user.username)
    
    check = check_inventory_exists(product_id,supplier_id,w_id)

    return JsonResponse({'exists': check})

@require_POST
def order_procurement(request):
    if request.method=='POST':
        product_id = request.POST.get('product')
        supplier_id = request.POST.get('supplier')
        quantity = request.POST.get('quantity')
        w_id=get_warehouse_id(request.user.username)
        unit_price=get_price_detail(product_id,supplier_id)
        contact_email = request.user.email

        check = check_inventory_exists(product_id,supplier_id,w_id)
        if check==False:
            #create an entry in inventory
            reorder_level = request.POST.get('reorder-level')
            result = add_inventory(product_id,supplier_id,w_id,reorder_level)
            if result is False:
                return redirect('/manager')
            print("Created inventory entry.")

        #insert these data in to requests table
        request_id = add_request(product_id,supplier_id,w_id,contact_email,unit_price,quantity)
        
        # Add into notifications here
        add_notification(request_id,supplier_id,'Supplier',context='RequestProcurement')
        add_notification(request_id,w_id,'Manager',context='RequestProcurement')
        
        return redirect('/manager')
    else:
        #should I remove it?
        product_details = get_products()
        context = {
            'products':product_details,
            'username':request.user.username,
        }
        return render(request,'manager_procurements.html',context)

def mark_all_notifications_read(request):
    if request.method=='POST':
        w_id = get_warehouse_id(request.user.username)
        set_notifications_read(id=w_id,type = "Manager")
        return redirect(request.META.get('HTTP_REFERER', '/'))