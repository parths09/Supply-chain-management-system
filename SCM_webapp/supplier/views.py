from django.shortcuts import render, redirect
from supplier.query import *
from django.contrib import messages
from django.http     import JsonResponse
import json
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from simulation.utils import *
from simulation.simulator import get_current_date
from datetime import timedelta
from datetime import datetime


def get_delivery_date(order_date,username, warehouse_id):
    # Implement the logic to get the delivery date based on order_date, sup_id, and warehouse_id
    supplier_id=get_id(username)
    current_day  = order_date
    current_day=datetime.fromisoformat(current_day)
    cost,steps=dijkstra(graph,f'S{supplier_id}',f'W{warehouse_id}')
    total_cost = cost+len(steps)
    delivery_date = current_day+timedelta(days=total_cost)
    delivery_date=datetime.strftime(delivery_date,"%Y-%m-%d")
    return delivery_date


def fetch_notifications(username):
    supplier_id=get_id(username)
    notifications = get_supplier_notifications(supplier_id)
    notifications_unread = False
    for note in notifications:
        if note['is_read']==False:
            notifications_unread=True
            break
    return notifications, notifications_unread

def add_procurement_function(username,request_id, quantity, order_date, delivery_date,warehouse_id):
    # Implement the logic to add procurement
            add_procurement(request_id, quantity, order_date, delivery_date)
            supplier_id=get_id(username)
            # ADD NOTIFICATION
            add_notification(request_id,supplier_id,'Supplier',context='RequestApproval')
            add_notification(request_id,warehouse_id,'Manager',context='RequestApproval')
            # ADD NOTIFICATION
            add_notification(request_id,supplier_id,'Supplier',context='ProcurementArriving')
            add_notification(request_id,warehouse_id,'Manager',context='ProcurementArriving')


# Create your views here.
def supplier_home(request):
    if request.method == 'POST' and request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
            if data.get('action') == 'accept':
                quantity = data['quantity']
                request_id = data['request_id']
                order_date = data['order_date']
                warehouse_id = data['warehouse_id']
                delivery_date = get_delivery_date(order_date,request.user.username, warehouse_id)
                print(quantity, request_id,  order_date, delivery_date)
                # Call the function to add procurement
                add_procurement_function(request.user.username,request_id, quantity, order_date, delivery_date,warehouse_id)
                # Add your database operation here

                return JsonResponse({'status': 'ok'})
            
            elif data.get('action') == 'deny':
                request_id = data['request_id']
                supplier_id=get_id(request.user.username)
                warehouse_id = data['warehouse_id']
                # Call the function to reject the request
                # Add your database operation here
                decline_request(request_id)

                add_notification(request_id,supplier_id,'Supplier',context='RequestApproval')
                add_notification(request_id,warehouse_id,'Manager',context='RequestApproval')

                return JsonResponse({'status': 'ok'})
            else:
                return JsonResponse({'error': 'Invalid JSON action'}, status=400)
            
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    if request.method == 'POST':
        return render(request, 'supplier_home.html', {'username': request.user.username})
    
    all_requests = fetch_requests(request.user.username)
    notifications, notifications_unread = fetch_notifications(request.user.username)
    order_date = get_current_date()
    profile = get_profile(request.user.username)

    context={
        'username': request.user.username,
        'requests': all_requests,
        'notifications': notifications,
        'notifications_unread': notifications_unread,
        'order_date': order_date,
        'profile': profile[0]
    }
    print(profile)
    return render(request, 'supplier_home.html', context)

def supplier_procurement(request):
        
    if request.method == 'POST':
        return render(request, 'supplier_procurements.html', {'username': request.user.username})
    all_procurements = fetch_procurement(request.user.username)
    notifications, notifications_unread = fetch_notifications(request.user.username)
    profile = get_profile(request.user.username)
    context= {
        'username': request.user.username,
        'procurements': all_procurements,
        'notifications': notifications,
        'notifications_unread': notifications_unread,
        'profile': profile[0]
    }
    print(all_procurements)
    return render(request, 'supplier_procurements.html', context)

def supplier_products(request):

    all_products=sup_products(username=request.user.username)
    filtered_products = all_products
    product_names=[names['name'] for names in  fetch_names()]
    notifications, notifications_unread = fetch_notifications(request.user.username)
    profile = get_profile(request.user.username)
    if request.method == 'POST' and request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
            if data.get('action') == 'edit':
                product_id = data['product_id']
                price = data['price']
                update_products(product_id, request.user.username,price)
                # messages.success(request, 'Product updated successfully!')
                return JsonResponse({'status': 'ok'})
            elif data.get('action') == 'delete':
                product_id = data['product_id']
                delete_products(product_id, request.user.username)
                # messages.success(request, 'Product deleted successfully!')
                return JsonResponse({'status': 'ok'})
            
            elif data.get('action') == 'exist_add':
                name = data['name']
                price = data['price']
                # if product_name not in product_names:
                #     messages.error(request, 'Product name does not exist.')
                #     return redirect('supplier_products')

                add_existing_products(name, request.user.username, price)
                # messages.success(request, 'Product added successfully!')
                return JsonResponse({'status': 'ok'})

            elif data.get('action') == 'new_add':
                name = data['name']
                price = data['price']
                description = data['description']
                category = data['category']
                add_new_product(request.user.username,name, price, description, category)
                # messages.success(request, 'Product added successfully!')
                return JsonResponse({'status': 'ok'})
            
            else:
                return JsonResponse({'error': 'Invalid JSON action'}, status=400)
            
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    # print(filtered_products)

    if request.method == 'POST':
        return render(request, 'supplier_products.html', {'username': request.user.username})
    

    context = {
            "username": request.user.username,
            "products": filtered_products,
            "existing_names": product_names,
            "notifications": notifications,
            "notifications_unread": notifications_unread,
            'profile': profile[0]      
            }
    
    return render(request, 'supplier_products.html', context)

def mark_all_notifications_read(request):
    if request.method=='POST':
        supplier_id=get_id(request.user.username)
        set_notifications_read(id=supplier_id,type = "Supplier")
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
@login_required
def change_password(request):
    if request.method == 'POST':
        old = request.POST['old_password']
        new = request.POST['new_password']
        confirm = request.POST['confirm_password']

        if new != confirm:
            messages.error(request, "New passwords do not match.")
            return redirect(request.META.get('HTTP_REFERER'))

        if not request.user.check_password(old):
            messages.error(request, "Old password is incorrect.")
            return redirect(request.META.get('HTTP_REFERER'))

        request.user.set_password(new)
        request.user.save()
        update_session_auth_hash(request, request.user)  # Keeps the user logged in
        messages.success(request, "Password changed successfully.")
        return redirect(request.META.get('HTTP_REFERER'))