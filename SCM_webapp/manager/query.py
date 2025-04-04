
from manager.db import db
PORT = 5432
DATABASE_NAME = 'supply_chain_management'
HOST = 'localhost'

def cus_shipments(name):

        """
        Function to get the shipments of customer
        cus_id:- customer id
        """

        n_query = f'''
        select customer_id from customers where name = '{name}';'''
        result = db.execute_dql_commands(n_query)
        for i in result:
            cus_id = i.customer_id

        try:
            query = f'''
            select * from get_orders({cus_id}) '''
            result = db.execute_dql_commands(query)
            shipments=result.mappings().all()
            return shipments

        except Exception as err:
            print(f'Failed to fetch customer shipments -- {err}')
