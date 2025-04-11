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
--set role customer;
--select * from get_orders('Alice Johnson');
--set role postgres;


--2)
drop owned by manager;
drop role manager;
create role manager with login password 'manager_pass';

grant select on managers to manager
grant select on inventory to manager
grant select on products to manager
grant select on suppliers to manager

