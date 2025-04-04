from django.urls import path
from . import views

urlpatterns = [
    path('',views.manager_home,name='manager_home'),
    path('shipments', views.manager_shipments, name='manager_shipments'),
]