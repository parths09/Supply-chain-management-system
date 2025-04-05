
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
