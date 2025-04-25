from django.urls import path
from . import views

urlpatterns = [
    # path('',views.customer_home,name='customer_home'),
    path('', views.customer_orders, name='customer_orders'),
    path('tracking-<str:tracking_number>-<str:detail_id>', views.tracking_page, name='tracking_page'),
    path('mark_all_notifications_read',views.mark_all_notifications_read,name='mark_all_notifications_read_customer'),
    path('change-password/', views.change_password, name='change_password_customer'),
]