-- Trigger to add notification when procurement is delivered

drop trigger if exists notify_procurement_trigger on procurements;
drop function  if exists notify_procurement ;

create or replace function notify_procurement()
returns trigger
language plpgsql as $$
declare
message1 text;
message2 text;
p_name varchar(50);
s_name varchar(150);
w_name varchar(50);
s_id bigint;
p_id bigint;
w_id integer;
qty integer;

begin
	if new.status='Delivered' then
	select pr.quantity, p.name,p.product_id,s.supplier_name,s.supplier_id,w.warehouse_id,w.name into qty,p_name,p_id,s_name,s_id,w_id,w_name
	from procurements pr
	join inventory i on pr.inventory_id = i.inventory_id
	join products p on p.product_id = i.product_id
	join suppliers s on s.supplier_id = i.supplier_id
	join warehouses w on w.warehouse_id = i.warehouse_id
	where pr.procurement_id = new.procurement_id;

	-- Change stock in inventory
	update inventory set quantity_in_stock = quantity_in_stock+qty
	where inventory_id=new.inventory_id;

	-- Change alert in inventory
	update inventory set alert = true 
	where inventory_id=new.inventory_id and alert = false;

	-- Add notification
	message1:=format('Your request for %s %s from %s has been DELIVERED.',qty,p_name,s_name);
	message2:=format('Procurement for %s %s from %s has been COMPLETED.',qty,p_name,w_name);
	
	insert into notifications(request_id,recipent_id,recipent_type,context,message) 
	values (new.procurement_id,w_id,'Manager','ProcurementDelivered',message1), 
		(new.procurement_id,s_id,'Supplier','ProcurementDelivered',message2);
	end if;
	return new;
end;
$$;

create or replace trigger notify_procurement_trigger
after update on procurements
for each row
execute procedure notify_procurement();


drop trigger if exists notify_customer_shipment_trigger on shippings;
drop function if exists notify_customer_shipment;

create or replace function notify_customer_shipment()
returns trigger
language plpgsql as $$
declare
message1 text;
trk varchar(15);
c_id bigint;

begin
	if new.shipping_status='Shipped' then
		select s.tracking_number,o.customer_id into trk,c_id
		from shippings s
		join order_details od on od.shipping_id = s.shipping_id
		join orders o on o.order_id = od.order_id
		where s.shipping_id = new.shipping_id;
			
		-- Add notification
		message1:=format('Your shipment with tracking number %s has been SHIPPED.',trk);
		
		insert into notifications(request_id,recipent_id,recipent_type,context,message) 
		values (NULL,c_id,'Customer','ShipmentShipped',message1);

	elsif new.shipping_status = 'Delivered' then
		select s.tracking_number,o.customer_id into trk,c_id
		from shippings s
		join order_details od on od.shipping_id = s.shipping_id
		join orders o on o.order_id = od.order_id
		where s.shipping_id = new.shipping_id;
			
		-- Add notification
		message1:=format('Your shipment with tracking number %s has been DELIVERED',trk);
		
		insert into notifications(request_id,recipent_id,recipent_type,context,message) 
		values (NULL,c_id,'Customer','ShipmentDelivered',message1);

	elsif new.shipping_status = 'Out for Delivery' then
		select s.tracking_number,o.customer_id into trk,c_id
		from shippings s
		join order_details od on od.shipping_id = s.shipping_id
		join orders o on o.order_id = od.order_id
		where s.shipping_id = new.shipping_id;
		
		-- Add notification
		message1:=format('Your shipment with tracking number %s is Out for Delivery.',trk);
		
		insert into notifications(request_id,recipent_id,recipent_type,context,message) 
		values (NULL,c_id,'Customer','ShipmentOutforDelivery',message1);
	
	end if;
	return new;
end;
$$;


create or replace trigger notify_customer_shipment_trigger
after update on shippings
for each row
execute procedure notify_customer_shipment();



drop trigger if exists order_completed_trigger on shippings;
drop function if exists update_order_status ;

create or replace function update_order_status()
returns trigger
language plpgsql as $$
declare
o_id bigint;
result boolean;

begin
	if new.shipping_status = 'Delivered' then
		select od.order_id into o_id
		from order_details od
		where od.shipping_id = new.shipping_id
		limit 1;
	
		result := check_order_completed(o_id);
	
		if result is true then
			raise notice 'Order id %d has been completed',o_id;
			update orders set order_status = 'Completed' where order_id = o_id;
		end if;
	end if;
	
	return new;
end;
$$;

create or replace trigger order_completed_trigger
after update on shippings
for each row
execute procedure update_order_status();



drop trigger if exists active_prices_trigger on prices;
drop function if exists activate_prices ;

create or replace function activate_prices()
returns trigger
language plpgsql as $$

begin
	new.active = True;
	return new;
end;
$$;

create or replace trigger active_prices_trigger
after update on prices
for each row
execute procedure activate_prices();