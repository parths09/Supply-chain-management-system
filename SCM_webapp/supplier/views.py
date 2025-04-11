from django.shortcuts import render, redirect
from supplier.query import *
from django.contrib import messages


# Create your views here.
def supplier_home(request):
    return render(request, 'supplier_home.html', {'username': request.user.username})

def supplier_products(request):

    all_products=sup_products(username=request.user.username)
    filtered_products = all_products
    # print(filtered_products)
    if request.method == 'POST':
        action = request.POST.get('action')  # Get the action type (edit or delete)
        # product_id = request.POST.get('product_id')  # Get the product ID
        # product = get_object_or_404(Product, id=product_id)

        if action == 'edit':
            product_id = request.POST.get('product_id')
            product_name = request.POST.get('name')
            price = request.POST.get('price')
            description = request.POST.get('description')
            category = request.POST.get('category')
            print(product_id, product_name, price, description)

            insert_products(product_id, request.user.username, product_name, price, description,category)
            
            # messages.success(request, 'Product updated successfully!')
            return redirect('supplier_products')
        elif action == 'delete':
            product_id = request.POST.get('product_id')
            print(product_id)
            messages.success(request, 'Product deleted successfully!')
            return redirect('supplier_products')
        elif action == 'add':
            pass

    context = {
            "username": request.user.username,
            "products": filtered_products,
            }
    
    return render(request, 'supplier_products.html', context)