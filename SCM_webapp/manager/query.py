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

def get_low_stock(warehouse_id):
     """
     Get details of products which are low in stock.
     """
     try:
         query = f'''select * from get_low_stock({warehouse_id})'''
         result = db.execute_dql_commands(query)
         low_stock = result.mappings().all()
         return low_stock
         
     except Exception as err:
          print(f'Failed to fetch low stock -- {err}')

def get_incoming_procurements(warehouse_id):
     """
     Get details of procurements arriving at a warehouse.
     """
     try:
         query = f'''select * from get_incoming_procurements({warehouse_id})'''
         result = db.execute_dql_commands(query)
         incoming_procurements = result.mappings().all()
         return incoming_procurements
         
     except Exception as err:
          print(f'Failed to fetch low stock -- {err}')

def update_ignore_alert(i_id):
     """
     Set value of 'alert' in inventory to false.
     """
     try:
         query = f'''update inventory set alert = false where inventory_id = {i_id}'''
         db.execute_ddl_and_dml_commands(query)
         
     except Exception as err:
          print(f'Failed to update ignore alert -- {err}')

def get_filtered_suppliers(product_id):
     """
     Get suppliers' data for a paricular product_id.
     """
     try:
         query = f'''select s.*
                    from suppliers s
                    join prices p on p.supplier_id = s.supplier_id
                    where p.product_id = {product_id}'''
         result = db.execute_dql_commands(query)
         data = result.mappings().all()
         return data
         
     except Exception as err:
          print(f'Failed to get filtered suppliers -- {err}')

def get_price_detail(product_id,supplier_id):
     """
     Get suppliers' data for a paricular product_id.
     """
     try:
         query = f'''select unit_price
                    from prices p
                    where p.product_id = {product_id} and p.supplier_id={supplier_id}
                    '''
         result = db.execute_dql_commands(query)
         price = list(list(result)[0])[0]
         return price
         
     except Exception as err:
          print(f'Failed to get filtered suppliers -- {err}')

def get_products():
     """
     Get all products' details.
     """
     try:
         query = f'''select *
                    from products p;
                    '''
         result = db.execute_dql_commands(query)
         result= result.mappings().all()
         return result
         
     except Exception as err:
          print(f'Failed to get filtered suppliers -- {err}')

def add_request(product_id,supplier_id,warehouse_id,contact_email,unit_price,quantity):
     """
     Add procurement request into requests table.
     """
     try:
          query = f'''
                    insert into requests(product_id,supplier_id,warehouse_id,contact_email,unit_price,quantity)
                    values ({product_id},{supplier_id},{warehouse_id},'{contact_email}',{unit_price},{quantity})
                    returning request_id;
                    ''' 
          result = db.execute_ddl_and_dml_commands(query)
          id = list(list(result)[0])[0]
          return id
         
     except Exception as err:
          print(f'Failed to add request -- {err}')

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

def get_manager_notifications(w_id):
     """
     Get all notification for a particular warehouse manager.
     """
     try:
         query = f'''select *
         from notifications n
         where n.recipent_type = 'Manager' and n.recipent_id = {w_id}
         order by created_at desc;
          '''
         result = db.execute_dql_commands(query)
         result= result.mappings().all()
         return result
         
     except Exception as err:
          print(f'Failed to get manager notifications -- {err}')

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

def check_inventory_exists(product_id,supplier_id,warehouse_id):
     """
     Check if combination exists in inventory.
     """
     try:
         query = f'''select exists(select * from inventory where
         product_id = {product_id} and supplier_id={supplier_id} and warehouse_id={warehouse_id});
          '''
         result = db.execute_dql_commands(query)
         result = list(list(result)[0])[0]
         return result
         
     except Exception as err:
          print(f'Failed to check existence of inventory -- {err}')

def add_inventory(product_id,supplier_id,warehouse_id,reorder_level):
     """
     Check if combination exists in inventory.
     """
     try:
         query = f'''insert into inventory(product_id,supplier_id,warehouse_id,reorder_level,quantity_in_stock)
         values ({product_id},{supplier_id},{warehouse_id},{reorder_level},0);
          '''
         result = db.execute_ddl_and_dml_commands(query)
         return result
         
     except Exception as err:
          print(f'Failed to add into inventory -- {err}')