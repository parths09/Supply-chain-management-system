--1)
drop owned by customer;
drop role customer;
create role customer with login password 'customer_pass';


grant select on customers to customer;
grant select on shippings to customer;
grant select on shipping_details to customer;
grant select on orders to customer;
grant select on order_details to customer;
grant select on customer_orders to customer;
grant select on products to customer;
grant select on suppliers to customer;
grant select on inventory to customer;
grant select on warehouses to customer;
grant select,update on notifications to customer;
grant select on customer_notifications to customer;
--set role customer;
--select * from get_orders('Alice Johnson');
--set role postgres;


--2)
drop owned by manager;
drop role manager;
create role manager with login password 'manager_pass';
grant select on managers to manager;
grant select,insert,update on inventory to manager;
grant select on products to manager;
grant select on suppliers to manager;
grant select on employees to manager;
grant select on warehouses to manager;
grant select on shippings to manager;
grant select on shipping_details to manager;
grant select on procurements to manager;
grant update on inventory to manager;
grant select on prices to manager;
grant select,insert on requests to manager;
GRANT USAGE, SELECT ON SEQUENCE requests_request_id_seq TO manager;
grant select,insert,update on notifications to manager;
GRANT USAGE, SELECT ON SEQUENCE notifications_notification_id_seq to manager;
GRANT USAGE, SELECT ON SEQUENCE inventory_inventory_id_seq to manager;
grant select on manager_notifications to manager;

--3)
drop owned by supplier ; 
drop role supplier;
create role supplier with login password 'supplier_pass';

grant all on products,prices  to supplier;
grant select on suppliers,inventory,warehouses,procurements,requests to supplier;

GRANT USAGE, SELECT ON SEQUENCE procurements_procurement_id_seq TO supplier;
grant select,insert,update on procurements to supplier;
grant select,insert,update on notifications to supplier;
grant select,update on requests to supplier;
GRANT USAGE, SELECT ON SEQUENCE notifications_notification_id_seq to supplier;
grant select on supplier_notifications to supplier;


