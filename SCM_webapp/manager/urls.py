from django.urls import path
from . import views

urlpatterns = [
    path('',views.manager_home,name='manager_home'),
    path('shipments', views.manager_shipments, name='manager_shipments'),
    path('stocks', views.manager_stocks, name='manager_stocks'),
    path('employees', views.manager_employees, name='manager_employees'),
    path('order_procurements', views.manager_procurements, name='manager_procurements'),
]