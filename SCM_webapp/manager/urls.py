from django.urls import path
from . import views

urlpatterns = [
    path('',views.manager_home,name='manager_home'),
    path('shipments', views.manager_shipments, name='manager_shipments'),
    path('stocks', views.manager_stocks, name='manager_stocks'),
    path('employees', views.manager_employees, name='manager_employees'),
    path('procurements', views.manager_procurements, name='manager_procurements'),
    path('order_procurement',views.order_procurement,name='order_procurements'),
    path('ignore_alert-<str:inventory_id>',views.ignore_alert,name='ignore_alert'),
    path('get_suppliers', views.get_suppliers, name='get_suppliers'),  # AJAX call
    path('get_price', views.get_price, name='get_price'),              # AJAX call
    path('mark_all_notifications_read',views.mark_all_notifications_read,name='mark_all_notifications_read'),
    path("check_inventory/", views.check_inventory, name="check_inventory"),

]