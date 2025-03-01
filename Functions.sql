--1)
--input : warehouse_id int
--returns the products present in the warehouse along with required attributes 

drop function if exists get_warehouse_products;

create or replace function get_warehouse_products(w_id int)

returns table (inventory_id int, product_id bigint, supplier_id bigint, quantity_in_stock int, 
reorder_level int) 

language plpgsql as $$

begin

	return query
	select i.inventory_id, i.product_id, i.supplier_id , i.quantity_in_stock,i.reorder_level from inventory as i
	where i.warehouse_id=w_id;
	
end;
$$;

select * from get_warehouse_products(3);



--2)
--input : customer_id
--returns the details of all orders of the customer

drop function if exists get_orders(cus_id bigint);

create or replace function get_orders(cus_id bigint)

returns table (tracking_number varchar(15),product_name varchar(50), supplier_name varchar(50), 
quantity int, amount numeric(10,2), status varchar(20))

language plpgsql as $$

begin 

	return query
	select shp.tracking_number, p.name, sup.name, od.quantity, od.amount, shp.shipping_status
	
	from products as p, suppliers as sup, order_details as od, orders as o , inventory as i,
	shippings as shp 
	
	where o.customer_id = cus_id  and o.order_id = od.order_id and 
	od.shipping_id = shp.shipping_id and od.inventory_id = i.inventory_id and 
	i.product_id= p.product_id and i.supplier_id = sup.supplier_id;

end;
$$;

select * from get_orders(1);


--3)
--input : warehouse_id
--returns the details of shipments currently in the warehouse



drop function if exists get_shipment_details;

create or replace function get_shipment_details(w_id int)

returns table (shp_id bigint, currently_in int, move_to int)
language plpgsql as $$

begin 

	return query
	with curr_shipment as (select distinct shipping_id, first_value (curr_warehouse) over w as curr_warehouse,
	first_value (next_warehouse) over w as next_warehouse
	
	from shipping_details 
	window w as (partition by shipping_id order by detail_id desc))
	
	select cs.shipping_id, curr_warehouse, next_warehouse from curr_shipment as cs,shippings as s 
	where cs.curr_warehouse=w_id and s.shipping_status = 'shipped' and s.shipping_id=cs.shipping_id;
	
end;
$$;

select * from get_shipment_details(2);






