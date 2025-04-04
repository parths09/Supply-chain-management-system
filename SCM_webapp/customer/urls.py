from django.urls import path
from . import views

urlpatterns = [
    path('',views.customer_home,name='customer_home'),
    path('shipments', views.customer_shipments, name='customer_shipments'),
    path('tracking/<str:tracking_number>/', views.tracking_page, name='tracking_page'),
]