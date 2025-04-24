from simulation.db import db

def add_shipping_detail(shipping_id,shipping_date,curr_warehouse,next_warehouse):
    """
    Function to get the shipments of customer
    cus_id:- customer id
    """
    try:
        if next_warehouse is not None:
            query = f'''insert into shipping_details(shipping_id,shipping_date,curr_warehouse,next_warehouse)
            values ({shipping_id},'{shipping_date}',{curr_warehouse},{next_warehouse})
            '''
        else:
            query = f'''insert into shipping_details(shipping_id,shipping_date,curr_warehouse,next_warehouse)
            values ({shipping_id},'{shipping_date}',{curr_warehouse},NULL)
            '''

        db.execute_ddl_and_dml_commands(query)
        
    except Exception as err:
        print(f'Failed to fetch customer shipments -- {err}')


def add_order(order_id,customer_id,order_date,total_amount,order_status):
    try:
        query = f'''insert into orders(order_id,customer_id,order_date,total_amount,order_status)
        values ({order_id},{customer_id},'{order_date}',{total_amount},'{order_status}');
        '''
        result=db.execute_ddl_and_dml_commands(query)
        return result
    except Exception as err:
        print(f'Failed to add order -- {err}')


def add_shipping(shipping_id,delivery_date,tracking_number,shipping_status,last_updated):
    try:
        query=f'''insert into shippings(shipping_id,delivery_date,tracking_number,shipping_status,last_updated)
        values ({shipping_id},'{delivery_date}','{tracking_number}','{shipping_status}','{last_updated}');
        '''
        db.execute_ddl_and_dml_commands(query)
        
    except Exception as err:
        print(f'Failed to add into shippings -- {err}')


def add_order_details(order_id,inventory_id,shipping_id,quantity,amount):
    try:
        query=f'''insert into order_details(order_id,inventory_id,shipping_id,quantity,amount)
        values ({order_id},{inventory_id},{shipping_id},{quantity},{amount});
        '''
        db.execute_ddl_and_dml_commands(query)
        
    except Exception as err:
        print(f'Failed to add into order_details -- {err}')


def get_current_position(shipping_id):
    """
    Function to get the shipments of customer
    cus_id:- customer id
    """
    try:
        query = f'''select curr_warehouse from shipping_details
        where shipping_id = {shipping_id}
        order by detail_id desc limit 1;
        '''
        result=db.execute_dql_commands(query)
        result = list(list(result)[0])[0]
        return result
        
    except Exception as err:
        print(f'Failed to fetch current position -- {err}')


def get_source(shipping_id):
    try:
        query = f'''select i.warehouse_id
        from shippings s
        join order_details od on s.shipping_id = od.shipping_id
        join inventory i on i.inventory_id = od.inventory_id
        where s.shipping_id = {shipping_id};
        '''
        result=db.execute_dql_commands(query)
        result = list(list(result)[0])[0]
        return result
        
    except Exception as err:
        print(f'Failed to fetch current position -- {err}')


def get_destination(shipping_id):
    try:
        query = f'''select o.customer_id
        from shippings s
        join order_details od on od.shipping_id = s.shipping_id
        join orders o on o.order_id = od.order_id
        where s.shipping_id = {shipping_id};
        '''
        result=db.execute_dql_commands(query)
        result = list(list(result)[0])[0]
        return f"C{result}"
        
    except Exception as err:
        print(f'Failed to fetch customer shipments -- {err}')




def get_warehouse_id(inventory_id):
    try:
        query = f'''select warehouse_id from inventory where inventory_id = {inventory_id};
        '''
        result=db.execute_dql_commands(query)
        result = list(list(result)[0])[0]
        return result
    except Exception as err:
        print(f'Failed to fetch warehouse id -- {err}')

def check_order_completed(order_id):
    # this function is not more used
    try:
        query = f'''select exists(select * 
        from order_details od
        join shippings s on s.shipping_id = od.shipping_id
        where shipping_status!='Delivered' and od.order_id = {order_id});
        '''
        result=db.execute_dql_commands(query)
        result = list(list(result)[0])[0]
        return not result
    except Exception as err:
        print(f'Failed to fetch warehouse id -- {err}')