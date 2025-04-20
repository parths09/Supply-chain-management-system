from django.contrib import admin
from .models import Shipment,Procurement,Order
# Register your models here.


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['shipping_id', 'delivery_date','tracking_number','shipping_status','last_updated']

@admin.register(Procurement)
class ProcurementAdmin(admin.ModelAdmin):
    list_display = ['procurement_id', 'inventory_id','quantity','order_date','delivery_date','status','last_updated']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer_id','order_date','total_amount','order_status']
