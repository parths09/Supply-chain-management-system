--SUPPLIER
--1)
drop procedure if exists update_products_supplier;

create or replace procedure  update_products_supplier(p_id bigint,u_name varchar(150) ,price numeric(10,2))
language plpgsql as $$
declare 
	sup_id bigint;
begin 
	select supplier_id into sup_id from suppliers where username=u_name;
	--raise notice 'id : %',sup_id;
	update prices set unit_price=price where product_id = p_id and supplier_id= sup_id;
end;
$$;

-- select * from get_supplier_products('techworld');

-- call update_products_supplier(1,'techworld',1400.00);
-- select * from get_supplier_products('techworld');

-- call update_products_supplier(1,'techworld',1200.00);


--2)
drop procedure if exists delete_products_supplier;

create or replace procedure delete_products_supplier(p_id bigint,u_name varchar(150))
language plpgsql as $$
declare 
	sup_id bigint;
begin 
	select supplier_id into sup_id from suppliers where u_name = username;
	-- raise notice 'id : %',sup_id;
	update prices set active=false where product_id = p_id and supplier_id= sup_id;

end;
$$;

-- select * from get_supplier_products('techworld');
-- call delete_products_supplier(1,'techworld');

-- select * from get_supplier_products('techworld');
-- update prices set active=true where product_id = 1 and supplier_id= 1;

-- select * from get_supplier_products('techworld');

--3)
drop procedure if exists add_new_products;

create or replace procedure  add_new_products(u_name varchar(150) ,price numeric(10,2),p_name varchar(50),pdescription text default NULL, 
pcategory text default NULL)
language plpgsql as $$
declare 
	sup_id bigint;
	prod_id bigint;
begin 
	select supplier_id into sup_id from suppliers where username=u_name;
	select product_id+1 into prod_id from products order by product_id desc limit 1;
	--raise notice 's_id : % ,p_id : %',sup_id,prod_id;
	insert into  products (product_id, name, description, category) VALUES
	(prod_id,p_name,pdescription,pcategory);
	insert into prices (product_id, supplier_id, unit_price,active) VALUES
	(prod_id,sup_id,price,true);
end;
$$;

-- call add_new_products('techworld',10.20,'ft');
-- delete  from products where name='ft';
-- delete from prices where product_id =6 and supplier_id = 1;
--4)

drop procedure if exists add_existing_products;

create or replace procedure add_existing_products(u_name varchar(150) ,price numeric(10,2),p_name varchar(50))
language plpgsql as $$
declare 
	sup_id bigint;
	prod_id bigint;
begin 
	select supplier_id into sup_id from suppliers where username=u_name;
	select product_id into prod_id from products where name=p_name;

	if exists(select * from prices where product_id = prod_id and supplier_id= sup_id) then 
		update prices set active=true where product_id = prod_id and supplier_id= sup_id;
		update prices set unit_price=price where product_id = prod_id and supplier_id= sup_id;
	else 
		insert into prices (product_id, supplier_id, unit_price,active) VALUES
		(prod_id,sup_id,price,true);
	end if;
end;
$$;

-- call delete_products_supplier(1,'techworld');
-- select * from prices;
-- select * from products;

-- call add_existing_products('techworld',1200,'Laptop');

drop procedure if exists add_procurement;
create or replace procedure add_procurement (req_id int, Quantity int, orderDate date, deliveryDate  date)
language plpgsql as $$
declare 
	inv_id int;
begin 
	select i.inventory_id into inv_id from inventory as i 
	join (select * from requests where request_id = req_id) as r 
	on i.supplier_id=r.supplier_id and i.product_id=r.product_id and i.warehouse_id=r.warehouse_id;
	--raise notice 'i_id : %',inv_id;
	
	update requests set approval ='Accepted' where request_id =req_id;

	insert into procurements (inventory_id,quantity,order_date,delivery_date,status) VALUES
	(inv_id,Quantity,orderDate,deliveryDate,'Processing');
	
end;
$$;

drop procedure if exists decline_request;
create or replace procedure decline_request (req_id int)
language plpgsql as $$
begin 
	update requests set approval ='Denied' where request_id =req_id;
end;
$$;
