--1)
drop index if exists supplier_notifications_idx ;
create index supplier_notifications_idx on notifications using hash(recipent_type) where recipent_type = 'Supplier';

explain analyze(select * from notifications  where recipent_type = 'Supplier');

--2)
drop index if exists manager_notifications_idx;
create index manager_notifications_idx on notifications using hash(recipent_type) where recipent_type = 'Manager';

select * from notifications  where recipent_type = 'Manager';

--3)
drop index if exists customer_notifications_idx ;
create index customer_notifications_idx on notifications using hash(recipent_type) where recipent_type = 'Customer';

select * from notifications  where recipent_type = 'Customer';

--4)
drop index if exists supplier_username_idx;
create index supplier_username_idx on suppliers using hash(username);

explain analyze (select p.name,p.product_id,p.description,ps.unit_price,p.category
	from products as  p join prices as  ps on p.product_id = ps.product_id
	join suppliers  as s on ps.supplier_id = s.supplier_id where s.username = 'techworld' and ps.active=true);

explain analyze(select * from get_supplier_products('techworld'));