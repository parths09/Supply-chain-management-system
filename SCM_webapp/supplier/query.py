from supplier.db import db

def sup_products(username):
    try:
        query = f''' select * from get_supplier_products('{username}');'''
        result = db.execute_dql_commands(query)
        products = list(result.mappings().all())
        return products
    except Exception as err:
        print(f'Failed to fetch product details -- {err}')    

def update_products(product_id,username,price):
    try:
        query = f''' call update_products_supplier({product_id},'{username}',{price});'''
        result = db.execute_ddl_and_dml_commands(query)
        return result
    except Exception as err:
        print(f'Failed to insert product details -- {err}')

def delete_products(product_id,username):
    try:
        query = f''' call delete_products_supplier({product_id},'{username}');'''
        result = db.execute_ddl_and_dml_commands(query)
        return result
    except Exception as err:
        print(f'Failed to insert product details -- {err}')

def fetch_names():
    try:
        query = f''' select name from products;'''
        result = db.execute_dql_commands(query)
        names = list(result.mappings().all())
        return names
    except Exception as err:
        print(f'Failed to fetch product details -- {err}')

def add_new_product(username, name, price, description, category):
    try:
        query = f''' call add_new_products('{username}',{price},'{name}','{description}','{category}');'''
        result = db.execute_ddl_and_dml_commands(query)
        return result
    except Exception as err:
        print(f'Failed to insert product details -- {err}')


def add_existing_products(product_name,username,price):
    try:
        product_name=product_name.strip()
        print(product_name)
        query = f''' call add_existing_products('{username}',{price},'{product_name}');'''
        result = db.execute_ddl_and_dml_commands(query)
        return result
    except Exception as err:
        print(f'Failed to insert product details -- {err}')


def fetch_procurement(username):
    try:
        query = f''' select * from get_procurements_supplier('{username}');'''
        result = db.execute_dql_commands(query)
        products = list(result.mappings().all())
        return products
    except Exception as err:
        print(f'Failed to fetch product details -- {err}')

def fetch_requests(username):
    try:
        query = f''' select * from get_requests_supplier('{username}');'''
        result = db.execute_dql_commands(query)
        products = list(result.mappings().all())
        return products
    except Exception as err:
        print(f'Failed to fetch product details -- {err}')

def add_procurement(request_id, quantity,orderDate,deliverDate):
    try:
        query = f''' call add_procurement({request_id},{quantity},'{orderDate}','{deliverDate}');'''
        print(query)
        result = db.execute_ddl_and_dml_commands(query)
        return result
    except Exception as err:
        print(f'Failed to insert product details -- {err}')

def decline_request(request_id):
    try:
        query = f''' call decline_request({request_id});'''
        result = db.execute_ddl_and_dml_commands(query)
        return result
    except Exception as err:
        print(f'Failed to insert product details -- {err}')

def get_id(username):
    try:
        query = f''' select supplier_id from suppliers where username ='{username}';'''
        result = db.execute_dql_commands(query)
        id = list(result.mappings().all())
        return id[0]['supplier_id']
    except Exception as err:
        print(f'Failed to fetch product details -- {err}')

def get_supplier_notifications(sup_id):
     """
     Get all notification for a particular warehouse manager.
     """
     print(f'Fetching notifications for supplier {sup_id}')
     try:
         query = f'''select *
         from notifications n
         where n.recipent_type = 'Supplier' and n.recipent_id = {sup_id}
         order by created_at desc;
          '''
         result = db.execute_dql_commands(query)
         result= result.mappings().all()
         return result
         
     except Exception as err:
          print(f'Failed to get manager notifications -- {err}')