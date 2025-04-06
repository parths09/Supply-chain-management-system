
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
        print(f'Failed to fetch order date -- {err}')

