delete from shipping_details;
delete from order_details;
delete from shippings;
delete from orders;
delete from procurements;

INSERT INTO procurements (inventory_id,quantity,order_date,delivery_date,status) VALUES
(1,2,'2025-04-16','2025-04-18','Processing'),
(6,100,'2025-04-16','2025-04-18','In transit'),
(2,3,'2025-04-12','2025-04-14','Processing'),
(4,2,'2025-04-11','2025-04-17','In transit'),
(4,1,'2025-04-12','2025-04-15','In transit'),
(3,5,'2025-04-16','2025-04-18','Processing');