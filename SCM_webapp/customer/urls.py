from django.urls import path
from . import views

urlpatterns = [
    path('',views.customer_home,name='customer_home'),
    path('orders', views.customer_orders, name='customer_orders'),
    path('tracking-<str:tracking_number>', views.tracking_page, name='tracking_page'),
]