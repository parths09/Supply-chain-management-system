from manager.db import db

def get_warehouse_id(username):
    """
    Function to get the warehouse_id corressponding to a manager.

    username:- Username of the manager
    """
     
    try:
         query = f'''select warehouse_id from managers where username = '{username}';'''
         result = db.execute_dql_commands(query)
         w_id=list(list(result)[0])[0]
         return w_id
         
    except Exception as err:
         print(f'Failed to fetch customer shipments -- {err}')


def get_warehouse_products(warehouse_id):
    """
    Function to get the warehouse_id corressponding to a manager.

    username:- Username of the manager
    """
     
    try:
         query = f'''select * from get_warehouse_products('{warehouse_id}');'''
         result = db.execute_dql_commands(query)
         warehouse_products = result.mappings().all()
         return warehouse_products
         
    except Exception as err:
         print(f'Failed to fetch customer shipments -- {err}')
