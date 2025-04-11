--SUPPLIER
--1)
drop procedure if exists update_products_supplier;

create or replace procedure  update_products_supplier(p_id bigint,u_name varchar(150) ,price numeric(10,2) , p_name varchar(50)default NULL,description text default NULL, 
category text default NULL)
language plpgsql as $$
declare 
	sup_id bigint;
begin 
	select supplier_id into sup_id from suppliers where u_name = username;
	-- raise notice 'id : %',sup_id;
	update prices set unit_price = price where product_id = p_id and supplier_id= sup_id;
end;
$$;

select * from get_supplier_products('techworld');

call update_products_supplier(1,'techworld',1400.00);
select * from get_supplier_products('techworld');

call update_products_supplier(1,'techworld',1200.00);
	