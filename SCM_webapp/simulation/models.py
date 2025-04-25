from django.db import models

# Create your models here.



class Product(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'products'
        managed = False


class Supplier(models.Model):
    supplier_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=150)
    supplier_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15, unique=True)
    email_id = models.CharField(max_length=30, unique=True)
    address = models.TextField(null=True, blank=True)
    pincode = models.IntegerField()

    class Meta:
        db_table = 'suppliers'
        managed = False


class Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'prices'
        managed = False


class Customer(models.Model):
    customer_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.SmallIntegerField()
    phone_number = models.CharField(max_length=15, unique=True)
    email_id = models.CharField(max_length=30, unique=True)
    pincode = models.IntegerField()
    billing_address = models.TextField(null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'customers'
        managed = False


class Warehouse(models.Model):
    warehouse_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    pincode = models.IntegerField()

    class Meta:
        db_table = 'warehouses'
        managed = False


class Employee(models.Model):
    employee_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email_id = models.CharField(max_length=50, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    role = models.CharField(max_length=20)

    class Meta:
        db_table = 'employees'
        managed = False


class Manager(models.Model):
    manager_id = models.BigIntegerField(primary_key=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        db_table = 'managers'
        managed = False


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.RESTRICT)
    quantity_in_stock = models.IntegerField()
    reorder_level = models.IntegerField(null=True, blank=True)
    alert = models.BooleanField(default=True)

    class Meta:
        db_table = 'inventory'
        managed = False

class Shipment(models.Model):
    shipping_id = models.AutoField(primary_key=True)
    delivery_date = models.DateField(auto_now=False, auto_now_add=False)
    tracking_number = models.CharField(max_length=15)
    shipping_status = models.CharField(max_length=20)
    last_updated = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        managed = False  # ✅ Important: don't let Django manage it
        db_table = 'shippings'  # Match your actual table name

class Procurement(models.Model):
    PROCUREMENT_STATUS_CHOICES = [
        ('Delivered', 'Delivered'),
        ('In transit', 'In transit'),
        ('Processing', 'Processing'),
    ]

    procurement_id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE,db_column='inventory_id')
    quantity = models.IntegerField()
    order_date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=PROCUREMENT_STATUS_CHOICES,
        default='Processing'
    )
    last_updated = models.DateField(null=True, blank=True)

    class Meta:
        managed = False  # ✅ Important: don't let Django manage it
        db_table = 'procurements'  # Match your actual table name

    def __str__(self):
        return f"Procurement {self.procurement_id} - {self.status}"
    

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('On the way', 'On the way'),
        ('Completed', 'Completed'),
    ]

    order_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,db_column='customer_id') # Adjust app name if needed
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    order_status = models.CharField(max_length=15, choices=ORDER_STATUS_CHOICES, default='Pending')
    class Meta:
        managed = False  # ✅ Important: don't let Django manage it
        db_table = 'orders'  # Match your actual table name
    def __str__(self):
        return f"Order {self.order_id} - {self.order_status}"



class ShippingDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    shipping = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    shipping_date = models.DateField(null=True, blank=True)
    curr_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='curr_warehouse',db_column='curr_warehouse')
    next_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True, related_name='next_warehouse',db_column='next_warehouse')

    class Meta:
        db_table = 'shipping_details'
        managed = False


class OrderDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    inventory = models.ForeignKey(Inventory, on_delete=models.RESTRICT)
    shipping = models.ForeignKey(Shipment, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_details'
        managed = False


class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    contact_email = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    approval = models.CharField(max_length=20, default='Pending')

    class Meta:
        db_table = 'requests'
        managed = False


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    recipent_id = models.BigIntegerField()
    recipent_type = models.CharField(max_length=20)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    context = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notifications'
        managed = False