-- 1) Function: get_warehouse_products
-- Input: warehouse_id (int) - The ID of the warehouse.
-- Output: A table containing the inventory details of products currently in the specified warehouse

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


-- 2) Function: get_orders
-- Input: cus_id (bigint) - The ID of the customer.
-- Returns: A table containing details of all orders placed by the specified customer

drop function if exists get_orders(id bigint default NULL , u_name varchar(30) default NULL )

create or replace function get_orders(id bigint default NULL , u_name varchar(30) default NULL )

returns table (tracking_number varchar(15),product_name varchar(50),
quantity int, amount numeric(10,2), status varchar(20))

language plpgsql as $$
declare 
	cus_id bigint;

begin 
	cus_id = coalesce(id,(select customer_id from customers where name=u_name));
	return query
	select co.tracking_number,co.name,co.quantity,
	co.amount,co.order_status from customer_orders as co where customer_id = cus_id;
end;
$$;

select * from get_orders(1);

select * from get_orders(NULL,'Alice Johnson');


-- 3) Function: get_shipment_details
-- Input: w_id (int) - The ID of the warehouse.
-- Returns: A table containing details of shipments currently stationed at the specified warehouse


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






