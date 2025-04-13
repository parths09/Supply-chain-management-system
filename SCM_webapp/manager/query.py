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
         print(f'Failed to fetch warehouse id -- {err}')

def get_warehouse_name(w_id):
     """
    Function to get the warehouse name corressponding to a warehouse_id.

    """
     
     try:
          query = f'''select name from warehouses where warehouse_id = '{w_id}';'''
          result = db.execute_dql_commands(query)
          w_name=list(list(result)[0])[0]
          return w_name
          
     except Exception as err:
          print(f'Failed to fetch warehouse id -- {err}')


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
         print(f'Failed to fetch warehouse products -- {err}')

def get_employees(warehouse_id):
     """
     Get employees corresponding to a specific warehouse ID.
     """
     try:
         query = f'''select employee_id,first_name||' '||last_name as name,phone_number,email_id,salary,role
                    from employees where warehouse_id = {warehouse_id};'''
         result = db.execute_dql_commands(query)
         employees = result.mappings().all()
         return employees
         
     except Exception as err:
          print(f'Failed to fetch warehouse products -- {err}')

def get_active_shipments(warehouse_id):
     """
     Get details of shipments currently stationed at the specified warehouse.
     """
     try:
         query = f'''select * from get_shipment_details({warehouse_id})'''
         result = db.execute_dql_commands(query)
         active_shipments = result
         return active_shipments
         
     except Exception as err:
          print(f'Failed to fetch warehouse products -- {err}')

