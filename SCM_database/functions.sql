-- 1) Function: get_warehouse_products
-- Input: warehouse_id (int) - The ID of the warehouse.
-- Output: A table containing the inventory details of products currently in the specified warehouse

drop function if exists get_warehouse_products;

create or replace function get_warehouse_products(w_id int)

returns table (inventory_id int, product_name varchar(50), supplier_name varchar(150), quantity_in_stock int, 
reorder_level int) 

language plpgsql as $$

begin

	return query
	select i.inventory_id, p.name as product_name, s.supplier_name as supplier_name , i.quantity_in_stock,i.reorder_level
	from inventory as i
	join products p on p.product_id = i.product_id
	join suppliers s on s.supplier_id = i.supplier_id
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
quantity int, amount numeric(10,2), status varchar(20),detail_id integer)

language plpgsql as $$
declare 
	cus_id bigint;

begin 
	cus_id = coalesce(id,(select customer_id from customers where username=u_name));
	return query
	select co.tracking_number,co.name,co.quantity,
	co.amount,co.shipping_status,co.detail_id from customer_orders as co where customer_id = cus_id;

end;
$$;

select * from get_orders(1);

select * from get_orders(NULL,'Alice Johnson');


-- 3) Function: get_shipment_details
-- Input: w_id (int) - The ID of the warehouse.
-- Returns: A table containing details of shipments currently stationed at the specified warehouse


drop function if exists get_shipment_details;

create or replace function get_shipment_details(w_id int)

returns table (shp_id bigint, move_to integer,shipping_status varchar(20),tracking_number varchar(15),delivery_date date)
language plpgsql as $$

begin 

	return query
	with curr_shipment as (select distinct shipping_id, first_value (curr_warehouse) over w as curr_warehouse,
	first_value (next_warehouse) over w as next_warehouse
	
	from shipping_details 
	window w as (partition by shipping_id order by detail_id desc))
	
	select cs.shipping_id,next_warehouse, s.shipping_status,s.tracking_number,s.delivery_date
	from curr_shipment as cs
	join shippings as s on cs.shipping_id =s.shipping_id
	where cs.curr_warehouse=w_id and s.shipping_status in ('Shipped','Pending','Processing',null);
	
end;
$$;

select * from get_shipment_details(2);

-- 4) Function: get_tracking
-- Input: trk (varchar(15)) - The tracking number of the shipment.
-- Returns: A table containing shipping details including current location and destination warehouse

drop function if exists get_tracking;

create or replace function get_tracking(trk varchar(15))
returns table(shipping_id bigint, date date, currently_in integer, move_to integer,warehouse_name varchar(50))
language plpgsql as $$
begin 

	return query
	select s.shipping_id,sd.shipping_date,sd.curr_warehouse,sd.next_warehouse,w.name
	from shippings s
	join shipping_details sd on s.shipping_id = sd.shipping_id
	join warehouses w on w.warehouse_id = sd.curr_warehouse
	where s.tracking_number = trk;
	
end;
$$;

-- 5) Function: get_order_date
-- Input: trk (varchar(15)) - The tracking number of the shipment.
-- Returns: The order date (date) for the specified tracking number
drop function if exists get_order_date;

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



-- 6) Function: get_product_details
-- Input: trk (varchar(15)) - The tracking number of the shipment.
-- Returns: A table containing comprehensive product, supplier and shipping details for the specified tracking number

drop function if exists get_product_details;

create or replace function get_product_details(trk varchar(15),d_id integer)
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
	where s.tracking_number=trk and od.detail_id = d_id;
end;
$$;


--SUPPLIER FUNCTIONS


-- 7) Function: get_supplier_products
-- Input: u_name (varchar(150)) - The username of the supplier.
-- Returns: A table containing product details available from the specified supplier
drop function if exists get_supplier_products ;

create or replace function get_supplier_products(u_name varchar (150))

returns table( name varchar(50) ,id bigint,description text ,price numeric(10,2),category text)
language plpgsql as $$

begin 
	return query
	
	select p.name,p.product_id,p.description,ps.unit_price,p.category
	from products as  p join prices as  ps on p.product_id = ps.product_id
	join suppliers  as s on ps.supplier_id = s.supplier_id where s.username = u_name and ps.active=true;

end;
$$;

select * from get_supplier_products('techworld');


-- 8) Function: get_procurements_supplier
-- Input: sup_name (varchar) - The username of the supplier.
-- Returns: A table containing procurement details for the specified supplier including warehouse and product information

drop function if exists get_procurements_supplier;

create or replace function get_procurements_supplier(sup_name varchar)
returns TABLE(warehouse_name varchar , warehouse_location varchar,quantity integer, order_date date, delivery_date date,
status varchar, product_name varchar)
language plpgsql as $$
begin 
	return query
	select w.name,w.location,p.quantity,p.order_date,p.delivery_date,p.status,pr.name
	from procurements p
	join inventory i on i.inventory_id = p.inventory_id
	join products pr on pr.product_id = i.product_id
	join suppliers s on s.supplier_id = i.supplier_id
	join warehouses w on i.warehouse_id = w.warehouse_id
	where s.username = sup_name ;
end;
$$;

select * from get_procurements_supplier('techworld');


-- 9) Function: get_requests_supplier
-- Input: sup_name (varchar) - The username of the supplier.
-- Returns: A table containing pending request details for the specified supplier including warehouse and product information
drop function if exists get_requests_supplier;

create or replace function get_requests_supplier(sup_name varchar)
returns table(id int , w_id int,warehouse_name varchar , warehouse_location varchar,quantity integer,  product_name varchar,
contact varchar,unit_price numeric (10,2),total numeric (10,2))
language plpgsql as $$
begin
	return query
	select r.request_id,w.warehouse_id,w.name,w.location,r.quantity,p.name,r.contact_email,r.unit_price,(r.unit_price * r.quantity)
	from requests as r 
	join (select * from suppliers where username=sup_name) as s on r.supplier_id = s.supplier_id
	join warehouses as w on w.warehouse_id=r.warehouse_id
	join products as p on p.product_id=r.product_id
	where r.approval in('Pending');
end;
$$;

select * from get_requests_supplier('techworld');


-- 10) Function: supplier_profile
-- Input: sup_name (varchar) - The username of the supplier.
-- Returns: A table containing contact and address details for the specified supplier

drop function if exists supplier_profile;

create or replace function supplier_profile(sup_name varchar)
returns table(name varchar, phone_number varchar,email varchar, address text,pincode integer) 
language plpgsql as $$
begin 
	return query
	select  s.supplier_name,s.phone_number,s.email_id, s.address,s.pincode
	from suppliers as s where s.username = sup_name;
end;
$$;

select * from supplier_profile('techworld');
 
-- 11) Function: get_low_stock
-- Input: w_id (int) - The ID of the warehouse.
-- Returns: A table containing inventory items with stock levels at or below reorder level in the specified warehouse



drop function if exists get_low_stock;

create or replace function get_low_stock(w_id int)
returns TABLE(inventory_id integer, supplier_id bigint, product_id bigint, product_name character varying, 
supplier_name character varying, quantity_in_stock integer, reorder_level integer,alert boolean)
language plpgsql as $$
begin 
	return query
	select i.inventory_id,i.supplier_id,i.product_id,p.name as product_name,s.supplier_name,i.quantity_in_stock,i.reorder_level,i.alert
	from inventory i
	join products p on p.product_id = i.product_id
	join suppliers s on s.supplier_id = i.supplier_id
	where warehouse_id = w_id and i.quantity_in_stock<=i.reorder_level;
end;
$$;

-- 12) Function: get_incoming_procurements
-- Input: w_id (int) - The ID of the warehouse.
-- Returns: A table containing details of incoming procurements (in transit or processing) for the specified warehouse

drop function if exists get_incoming_procurements;

create or replace function get_incoming_procurements(w_id int)
returns TABLE(inventory_id bigint, quantity integer, order_date date, delivery_date date,
status character varying, product_name character varying, supplier_name character varying)
language plpgsql as $$
begin 
	return query
	select p.inventory_id,p.quantity,p.order_date,p.delivery_date,p.status,pr.name as product_name,s.supplier_name
	from procurements p
	join inventory i on i.inventory_id = p.inventory_id
	join products pr on pr.product_id = i.product_id
	join suppliers s on s.supplier_id = i.supplier_id
	where i.warehouse_id = w_id and p.status in ('In transit','Processing');
end;
$$;

-- Function: check_order_completed
-- Input: o_id (bigint) - The ID of the order to check.
-- Returns: A boolean value - Returns true if all shipments for the order are delivered, false otherwise.
drop function if exists check_order_completed;
create or replace function check_order_completed(o_id bigint)
returns boolean
language plpgsql as $$
declare
	result boolean;
begin
	select exists(select * 
        from order_details od
        join shippings s on s.shipping_id = od.shipping_id
        where shipping_status!='Delivered' and od.order_id = o_id) into result;
		return not result;
end;
$$;

select * from check_order_completed(1001);