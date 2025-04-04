--1)

drop view if exists cus_shipments;

create or replace view  cus_shipments as 
(
with curr_shipment as (select distinct shipping_id, first_value (curr_warehouse) over w as curr_warehouse,
first_value (next_warehouse) over w as next_warehouse from shipping_details 
window w as (partition by shipping_id order by detail_id desc))
	
select cs.shipping_id, curr_warehouse, next_warehouse from curr_shipment as cs,shippings as s 
where  s.shipping_status = 'shipped' and s.shipping_id=cs.shipping_id
);

select * from cus_shipments;