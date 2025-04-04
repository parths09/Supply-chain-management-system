--1)

drop view if exists cus_shipments;

create or replace view  cus_shipments as 
(
	select o.customer_id ,shp.tracking_number, p.name, sup.name as sup_name, od.quantity, od.amount, shp.shipping_status
	from products as p, suppliers as sup, order_details as od, orders as o , inventory as i,
	shippings as shp where o.order_id = od.order_id and 
	od.shipping_id = shp.shipping_id and od.inventory_id = i.inventory_id and 
	i.product_id= p.product_id and i.supplier_id = sup.supplier_id
);

select * from cus_shipments;

