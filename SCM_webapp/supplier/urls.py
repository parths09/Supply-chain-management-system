from django.urls import path
from . import views

urlpatterns = [
    path('',views.supplier_home,name='supplier_home'),
    path('products/', views.supplier_products, name='supplier_products'),
]