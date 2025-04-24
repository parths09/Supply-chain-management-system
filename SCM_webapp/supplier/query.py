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
        print(f'Failed to fetch supplier_id details -- {err}')

def get_supplier_notifications(sup_id):
     """
     Get all notification for a particular warehouse manager.
     """
     print(f'Fetching notifications for supplier {sup_id}')
     try:
         query = f'''select *
         from supplier_notifications n
         where n.recipent_id = {sup_id}
         order by created_at desc;
          '''
         result = db.execute_dql_commands(query)
         result= result.mappings().all()
         return result
         
     except Exception as err:
          print(f'Failed to get supplier notifications -- {err}')


def set_notifications_read(id,type):
     """
     Set all notification as read.
     """
     try:
         query = f'''update notifications set is_read = true
           where recipent_type='{type}' and recipent_id = {id};
          '''
         db.execute_ddl_and_dml_commands(query)
         
     except Exception as err:
          print(f'Failed to mark all notifications read -- {err}')


def get_request_info(request_id):
     """
     Get product_name,supplier_name,warehouse_name, approval and quantity for particular request.
     """
     try:
         query = f'''select p.name as product_name,s.supplier_name,r.quantity,w.name as warehouse_name,r.approval
         from requests r
         join products p on r.product_id = p.product_id
         join suppliers s on r.supplier_id = s.supplier_id
         join warehouses w on r.warehouse_id = w.warehouse_id
         where r.request_id = {request_id};
          '''
         result = db.execute_dql_commands(query)
         result= result.mappings().all()[0]
         return result
         
     except Exception as err:
          print(f'Failed to get request info -- {err}')

def add_notification(request_id,recipent_id,recipent_type,context):
     """
     Add procurement request into requests table.
     """
     try:
          request_info = get_request_info(request_id)
          # formulate message:
          if recipent_type=='Manager':
               # Get info about product_name,supplier_name and quantity
               if context=='RequestProcurement':
                    message = f"You requested for {request_info['quantity']} {request_info['product_name']} from {request_info['supplier_name']}."
               elif context=='RequestApproval':
                    if request_info['approval']=='Accepted':
                         message=f"Your request for {request_info['quantity']} {request_info['product_name']} from {request_info['supplier_name']} has been ACCEPTED."
                    elif request_info['approval']=='Denied':
                         message=f"Your request for {request_info['quantity']} {request_info['product_name']} from {request_info['supplier_name']} has been DENIED."
               elif context=="ProcurementArriving":
                    message=f"Your request for {request_info['quantity']} {request_info['product_name']} from {request_info['supplier_name']} is ARRIVING."
               elif context=="ProcurementDelivered":
                    # this is handled by trigger
                    pass
          
          elif recipent_type=='Supplier':
               if context=='RequestProcurement':
                    message=f"Procurement request for {request_info['quantity']} {request_info['product_name']} from {request_info['warehouse_name']}."
               elif context=='RequestApproval':
                    if request_info['approval']=='Accepted':
                         message=f"You ACCEPTED request for {request_info['quantity']} {request_info['product_name']} from {request_info['supplier_name']}."
                    elif request_info['approval']=='Denied':
                         message=f"You DENIED request for {request_info['quantity']} {request_info['product_name']} from {request_info['supplier_name']}."
               elif context=="ProcurementArriving":
                    message=f"Procurement process for {request_info['quantity']} {request_info['product_name']} from {request_info['supplier_name']} has STARTED."
               elif context=="ProcurementDelivered":
                    # this is handled by trigger
                    pass

          query = f'''insert into notifications(request_id,recipent_id,recipent_type,context,message)
          values ({request_id},{recipent_id},'{recipent_type}','{context}','{message}');
          ''' 
          db.execute_ddl_and_dml_commands(query)
         
     except Exception as err:
          print(f'Failed to add notification -- {err}')

def get_profile(username):
    try:
        query = f''' select * from supplier_profile('{username}');'''
        result = db.execute_dql_commands(query)
        profile = list(result.mappings().all())
        return profile
    except Exception as err:
        print(f'Failed to fetch product details -- {err}')