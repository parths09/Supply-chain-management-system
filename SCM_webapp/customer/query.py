# import models here and write queries
from customer.db import db

def cus_orders(id=None,name=None):

    """
    Function to get the shipments of customer
    cus_id:- customer id
    """

    try:
        id = id if id else 'NULL'
        name = name if name else 'NULL'
        query = f'''select * from get_orders({id},'{name}');'''
        result = db.execute_dql_commands(query)
        shipments=result.mappings().all()
        return shipments
        
    except Exception as err:
        print(f'Failed to fetch customer shipments -- {err}')

def cus_tracking(tracking_no):
    """
    """
    try:
        query = f''' select * from get_tracking('{tracking_no}');'''
        result = db.execute_dql_commands(query)
        tracking_details=result.mappings().all()
        return tracking_details
    except Exception as err:
        print(f'Failed to fetch tracking details -- {err}')

def cus_shipping_status(tracking_no):
    try:
        query = f''' select shipping_status from shippings where tracking_number = '{tracking_no}' ;'''
        result = db.execute_dql_commands(query)
        shipping_status=list(result)[0]
        return shipping_status
    except Exception as err:
        print(f'Failed to fetch shipping status  -- {err}')

def cus_order_date(tracking_no):
    try:
        query = f''' select * from get_order_date('{tracking_no}');'''
        result = db.execute_dql_commands(query)
        order_date = list(list(result)[0])[0]
        return order_date
    except Exception as err:
        print(f'Failed to fetch order date -- {err}')

def cus_expected_delivery(tracking_no):
    try:
        query = f''' select delivery_date from shippings where tracking_number = '{tracking_no}';'''
        result = db.execute_dql_commands(query)
        # delivery=result.mappings().all()
        delivery = list(list(result)[0])[0]
        return delivery
    except Exception as err:
        print(f'Failed to fetch expected delivery date -- {err}')

def cus_product_details(tracking_no,detail_id=None):
    try:
        if detail_id is None:
            query=f'''select od.order_id,p.name as product_name,p.description as product_description,sup.supplier_name as supplier_name,
            sup.address as supplier_address,od.quantity,od.amount as price,c.shipping_address,s.shipping_status,o.order_date,s.delivery_date
            from shippings s
            join order_details od on od.shipping_id=s.shipping_id
            join orders o on od.order_id = o.order_id
            join customers c on c.customer_id = o.customer_id
            join inventory i on i.inventory_id = od.inventory_id
            join products p on p.product_id = i.product_id
            join suppliers sup on sup.supplier_id = i.supplier_id
            where s.tracking_number='{tracking_no}';
            '''
            result = db.execute_dql_commands(query)
            product_details=list(result.mappings().all())[0]
            return product_details
        else:
            query = f''' select * from get_product_details('{tracking_no}',{detail_id});'''
            result = db.execute_dql_commands(query)
            product_details=list(result.mappings().all())
            return product_details

    except Exception as err:
        print(f'Failed to fetch product details -- {err}')

def get_customer_id(username):
    try:
        query = f''' select customer_id from customers where username = '{username}';'''
        result = db.execute_dql_commands(query)
        table_id = list(list(result)[0])[0]
        return table_id
    except Exception as err:
        print(f'Failed to fetch customer id -- {err}')


def set_notifications_read(id,type):
     """
     Set all notification as read.
     """
     try:
         query = f'''update notifications set is_read = true
           where recipent_type='{type}' and recipent_id = {id};
          '''
         db.execute_ddl_and_dml_commands(query)
         
     except Exception as err:
          print(f'Failed to mark all notifications read -- {err}')

def get_customer_notifications(id):
     """
     Get all notification for a particular warehouse manager.
     """
     try:
         query = f'''select *
         from customer_notifications n
         where n.recipent_id = {id}
         order by created_at desc;
          '''
         result = db.execute_dql_commands(query)
         result= result.mappings().all()
         return result
         
     except Exception as err:
          print(f'Failed to get manager notifications -- {err}')