--1)
drop owned by customer;
drop role customer;
create role customer with login password 'customer_pass';

grant select on cus_shipments to customer;
grant select on customers to customer;

--set role customer;
--select * from get_orders('Alice Johnson');
--set role postgres;


--2)
drop owned by manager;
drop role manager;
create role manager with login password 'manager_pass';


