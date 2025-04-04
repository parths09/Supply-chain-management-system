
from customer.db import db

def cus_shipments(name):

    """
    Function to get the shipments of customer
    cus_id:- customer id
    """

    try:
        query = f'''
        select * from get_orders('{name}') '''
        result = db.execute_dql_commands(query)
        shipments=result.mappings().all()
        return shipments
        
    except Exception as err:
        print(f'Failed to fetch customer shipments -- {err}')
