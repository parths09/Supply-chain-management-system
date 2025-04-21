from django.urls import path
from . import views

urlpatterns = [
    path('',views.supplier_home,name='supplier_home'),
    path('products/', views.supplier_products, name='supplier_products'),
    path('procurement/', views.supplier_procurement, name='supplier_procurement'),
    path('mark_all_notifications_read',views.mark_all_notifications_read,name='mark_all_notifications_read'),
    path('change-password/', views.change_password, name='change_password_supplier'),
]