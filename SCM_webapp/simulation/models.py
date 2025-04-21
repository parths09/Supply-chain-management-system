from django.db import models

# Create your models here.

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
    inventory_id = models.IntegerField()
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
    customer_id = models.BigIntegerField() # Adjust app name if needed
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    order_status = models.CharField(max_length=15, choices=ORDER_STATUS_CHOICES, default='Pending')
    class Meta:
        managed = False  # ✅ Important: don't let Django manage it
        db_table = 'orders'  # Match your actual table name
    def __str__(self):
        return f"Order {self.order_id} - {self.order_status}"
