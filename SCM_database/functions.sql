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

-- Input: cus_id (bigint) - The ID of the customer or Input: cus_id (bigint)  or  name (varchar(30)) - the name of the customer
-- Returns: A table containing details of all orders placed by the specified customer

drop function if exists get_orders(id bigint, u_name varchar(30));


create or replace function get_orders(id bigint default NULL , u_name varchar(30) default NULL )

returns table (tracking_number varchar(15),product_name varchar(50),
quantity int, amount numeric(10,2), status varchar(20))

language plpgsql as $$
declare 
	cus_id bigint;

begin 
	cus_id = coalesce(id,(select customer_id from customers where username=u_name));
	return query
	select co.tracking_number,co.name,co.quantity,
	co.amount,co.shipping_status from customer_orders as co where customer_id = cus_id;

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


-- Function to get tracking details from tracking number
drop function if exists get_tracking

create or replace function get_tracking(trk varchar(15))
returns table(shipping_id bigint, date date, currently_in integer, move_to integer)
language plpgsql as $$
begin 

	return query
	select s.shipping_id,sd.shipping_date,sd.curr_warehouse,sd.next_warehouse
	from shippings s
	join shipping_details sd on s.shipping_id = sd.shipping_id
	where s.tracking_number = trk;
	
end;
$$;


-- Function to get order date from tracking number
drop function if exists get_order_date

create or replace function get_order_date(trk varchar(15))
returns date
language plpgsql as $$
declare
orderdate date;
begin 
	select o.order_date  into orderdate
	from shippings s
	join order_details od on od.shipping_id = s.shipping_id
	join orders o on o.order_id = od.order_id
	where s.tracking_number = trk;
	return orderdate;
end;
$$;


-- Get product details
drop function if exists get_product_details;

create or replace function get_product_details(trk varchar(15))
returns table(order_id bigint,product_name varchar(50),product_description text,supplier_name varchar(50), supplier_address text,
quantity integer,price numeric(10,2), shipping_address text,shipping_status varchar(20), order_date date, expected_delivery date)
language plpgsql as $$
begin
	return query
	select od.order_id,p.name as product_name,p.description as product_description,sup.supplier_name as supplier_name,
	sup.address as supplier_address,od.quantity,od.amount as price,c.shipping_address,s.shipping_status,o.order_date,s.delivery_date
	from shippings s
	join order_details od on od.shipping_id=s.shipping_id
	join orders o on od.order_id = o.order_id
	join customers c on c.customer_id = o.customer_id
	join inventory i on i.inventory_id = od.inventory_id
	join products p on p.product_id = i.product_id
	join suppliers sup on sup.supplier_id = i.supplier_id
	where s.tracking_number=trk;
end;
$$;


--SUPPLIER FUNCTIONS

--1) 
drop function if exists get_supplier_products ;

create or replace function get_supplier_products(u_name varchar (150))

returns table( name varchar(50) ,id bigint,description text ,price numeric(10,2),category text)
language plpgsql as $$

begin 
	return query
	
	select p.name,p.product_id,p.description,ps.unit_price,p.category
	from products as  p join prices as  ps on p.product_id = ps.product_id
	join suppliers  as s on ps.supplier_id = s.supplier_id where s.username = u_name;

end;
$$;

select * from get_supplier_products('techworld');