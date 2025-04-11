from supplier.db import db

def sup_products(username):
    try:
        query = f''' select * from get_supplier_products('{username}');'''
        result = db.execute_dql_commands(query)
        products = list(result.mappings().all())
        return products
    except Exception as err:
        print(f'Failed to fetch product details -- {err}')    

def insert_products(product_id,username, name, price, description, category):
    try:
        query = f''' call update_products_supplier({product_id},'{username}',{price},'{name}','{description}','{category}');'''
        result = db.execute_ddl_and_dml_commands(query)
        return result
    except Exception as err:
        print(f'Failed to insert product details -- {err}')