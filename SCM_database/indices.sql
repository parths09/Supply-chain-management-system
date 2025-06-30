--1)
drop index if exists supplier_notifications_idx ;
create index supplier_notifications_idx on notifications using hash(recipent_type) where recipent_type = 'Supplier';

explain analyze(select * from notifications  where recipent_type = 'Supplier');

--2)
drop index if exists manager_notifications_idx;
create index manager_notifications_idx on notifications using hash(recipent_type) where recipent_type = 'Manager';

explain analyze(select * from notifications  where recipent_type = 'Manager';)

--3)
drop index if exists customer_notifications_idx ;
create index customer_notifications_idx on notifications using hash(recipent_type) where recipent_type = 'Customer';

explain analyze(select * from notifications  where recipent_type = 'Customer';)

--4)
drop index if exists supplier_username_idx;
create index supplier_username_idx on suppliers using hash(username);

explain analyze(select * from get_supplier_products('techworld'));

--5)
drop index if exists customer_username_idx;
create index customer_username_idx on customers using hash(username);

explain analyze (select customer_id from customers where username = 'alice_johnson');