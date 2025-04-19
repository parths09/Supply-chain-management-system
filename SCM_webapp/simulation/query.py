from simulation.db import db

def add_shipping_detail(shipping_id,shipping_date,curr_warehouse,next_warehouse):
    """
    Function to get the shipments of customer
    cus_id:- customer id
    """
    try:
        if next_warehouse is None:
            query = f'''insert into shipping_details(shipping_id,shipping_date,curr_warehouse,next_warehouse)
            values ({shipping_id},{shipping_date},{curr_warehouse},{next_warehouse})
            '''
        else:
            query = f'''insert into shipping_details(shipping_id,shipping_date,curr_warehouse,next_warehouse)
            values ({shipping_id},{shipping_date},{curr_warehouse},NULL)
            '''

        db.execute_ddl_and_dml_commands(query)
        
    except Exception as err:
        print(f'Failed to fetch customer shipments -- {err}')

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
        print(f'Failed to fetch customer shipments -- {err}')