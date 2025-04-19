from django.shortcuts import render, redirect
from supplier.query import *
from django.contrib import messages


# Create your views here.
def supplier_home(request):
    return render(request, 'supplier_home.html', {'username': request.user.username})

def suppler_procurement(request):
    if request.method == 'POST':
        return render(request, 'supplier_procurements.html', {'username': request.user.username})
    all_procurements = fetch_procurement(request.user.username)
    context= {
        'username': request.user.username,
        'procurements': all_procurements
    }
    print(all_procurements)
    return render(request, 'supplier_procurements.html', context)

def supplier_products(request):

    all_products=sup_products(username=request.user.username)
    filtered_products = all_products
    product_names=[names['name'] for names in  fetch_names()]
    # print(filtered_products)
    if request.method == 'POST':
        action = request.POST.get('action')  
        print(action)

        if action == 'edit':
            product_id = request.POST.get('product_id')
            price = request.POST.get('price')

            update_products(product_id, request.user.username,price)
            
            # messages.success(request, 'Product updated successfully!')
            return redirect('supplier_products')
        elif action == 'delete':
            product_id = request.POST.get('product_id')
            delete_products(product_id, request.user.username)
            print(product_id)

            # messages.success(request, 'Product deleted successfully!')
            return redirect('supplier_products')
        
        elif action == 'exist_add':
            name = request.POST.get('name')
            price = request.POST.get('price')

            # if product_name not in product_names:
            #     messages.error(request, 'Product name does not exist.')
            #     return redirect('supplier_products')
            
            add_existing_products(name, request.user.username, price)
            # messages.success(request, 'Product added successfully!')
            return redirect('supplier_products')

        elif action == 'new_add':
            name = request.POST.get('name')
            price = request.POST.get('price')
            description = request.POST.get('description')
            category = request.POST.get('category')
            add_new_product(request.user.username,name, price, description, category)
            # messages.success(request, 'Product added successfully!')
            return redirect('supplier_products')

    context = {
            "username": request.user.username,
            "products": filtered_products,
            "existing_names": product_names,
            }
    
    return render(request, 'supplier_products.html', context)