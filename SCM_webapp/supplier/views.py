from django.shortcuts import render

# Create your views here.
def supplier_home(request):
    return render(request, 'supplier_home.html', {'username': request.user.username})

def supplier_products(request):
    return render(request, 'supplier_products.html', {'username': request.user.username})