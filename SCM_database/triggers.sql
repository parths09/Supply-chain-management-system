-- Trigger to add notification when procurement is delivered

drop trigger notify_procurement_trigger on procurements;
drop function notify_procurement ;

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