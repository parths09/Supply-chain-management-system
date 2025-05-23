--1)

drop view if exists customer_orders;

create or replace view  customer_orders as 
(
	select o.customer_id, shp.tracking_number , p.name,od.quantity, od.amount, shp.shipping_status, shp.delivery_date,od.detail_id
	from products as p,order_details as od, orders as o , inventory as i,
	shippings as shp where o.order_id = od.order_id and 
	od.shipping_id = shp.shipping_id and od.inventory_id = i.inventory_id and 
	i.product_id= p.product_id
);

select * from customer_orders;

drop view if exists manager_notifications;
create or replace view  manager_notifications as 
(
	select * from notifications n where n.recipent_type = 'Manager'
);


drop view if exists supplier_notifications;
create or replace view  supplier_notifications as 
(
	select * from notifications n where n.recipent_type = 'Supplier'
);


drop view if exists customer_notifications;
create or replace view  customer_notifications as 
(
	select * from notifications n where n.recipent_type = 'Customer'
);
