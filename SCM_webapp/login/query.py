from login.db import db

def insert_customer(username,first_name,last_name, age, phone_number, email_id, pincode, billing_address, shipping_address):
    try:
        query = f''' call insert_customer('{username}','{first_name}','{last_name}',{age}::smallint,'{phone_number}','{email_id}',
        {pincode},'{billing_address}','{shipping_address}');'''
        result = db.execute_ddl_and_dml_commands(query)
        return result
    except Exception as err:
        print(f'Failed to insert customer details -- {err}')

def insert_supplier( supplier_name, phone_number, email_id, address, pincode,username):
    try:
        query = f''' call insert_supplier('{username}','{supplier_name}','{phone_number}','{email_id}',
        {pincode},'{address}');'''
        result = db.execute_ddl_and_dml_commands(query)
        return result
    except Exception as err:
        print(f'Failed to insert supplier details -- {err}')