--1)

drop view if exists customer_orders;

create or replace view  customer_orders as 
(
	select o.customer_id, shp.tracking_number , p.name,od.quantity, od.amount, shp.shipping_status, shp.delivery_date
	from products as p,order_details as od, orders as o , inventory as i,
	shippings as shp where o.order_id = od.order_id and 
	od.shipping_id = shp.shipping_id and od.inventory_id = i.inventory_id and 
	i.product_id= p.product_id
);

select * from customer_orders;

