from django.contrib import admin
from .models import *
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

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id','description', 'name', 'category']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['supplier_id', 'username', 'supplier_name', 'phone_number', 'email_id']

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['product', 'supplier', 'unit_price', 'active']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'username', 'first_name', 'last_name', 'phone_number']

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['warehouse_id', 'name', 'pincode']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'first_name', 'last_name', 'warehouse', 'role']

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['manager_id', 'warehouse', 'username']

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['inventory_id', 'product', 'supplier', 'warehouse', 'quantity_in_stock']

@admin.register(ShippingDetail)
class ShippingDetailAdmin(admin.ModelAdmin):
    list_display = ['detail_id', 'shipping', 'shipping_date', 'curr_warehouse', 'next_warehouse']

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['detail_id', 'order', 'inventory', 'shipping', 'quantity', 'amount']

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['request_id', 'product', 'supplier', 'warehouse', 'quantity', 'unit_price', 'approval']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['notification_id', 'request', 'recipent_id', 'recipent_type', 'is_read', 'created_at']