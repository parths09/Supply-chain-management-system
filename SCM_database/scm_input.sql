INSERT INTO products (product_id, name, description, category) VALUES
(1, 'Laptop', '15-inch, Intel i7, 16GB RAM', 'Electronics'),
(2, 'Office Chair', 'Ergonomic chair with lumbar support', 'Furniture'),
(3, 'Running Shoes', 'Lightweight with cushioned sole', 'Clothing'),
(4, 'Fiction Book', 'Bestselling novel', 'Books'),
(5, 'Teddy Bear', 'Soft plush toy for kids', 'Toys');

INSERT INTO suppliers (supplier_id, supplier_name, phone_number, email_id, address, pincode,username) VALUES
(1, 'TechWorld Ltd.', '9876543210', 'contact@techworld.com', '123 Tech Street, NY', 10001, 'techworld'),
(2, 'Furniture Hub', '9123456789', 'support@furnihub.com', '456 Wood Ave, LA', 90001, 'furniture_hub'),
(3, 'Nike Suppliers', '9988776655', 'nike@shoes.com', '789 Sport Lane, TX', 73301, 'nike_suppliers'),
(4, 'BookDepot', '8765432109', 'info@bookdepot.com', '101 Reading Blvd, SF', 94101, 'book_depot'),
(5, 'ToyLand Inc.', '7553311223', 'hello@toyland.com', '202 Happy St, FL', 33101, 'toyland');

INSERT INTO prices (product_id, supplier_id, unit_price,active) VALUES
(1, 1, 1200.00,TRUE),
(2, 2, 250.00,TRUE),
(3, 3, 90.00,TRUE),
(4, 4, 15.00,TRUE),
(5, 5, 30.00,TRUE);

INSERT INTO warehouses (warehouse_id, name, location, phone_number, pincode) VALUES
(1, 'Warehouse A', 'New York', '9876543211', 10001),
(2, 'Warehouse B', 'Los Angeles', '8765432102',90001),
(3, 'Warehouse C', 'Texas', '7654321093',73301),
(4, 'Warehouse D', 'San Francisco', '6543210984',94101),
(5, 'Warehouse E', 'Florida', '5432109875', 33101);

INSERT INTO employees (employee_id, first_name,last_name, warehouse_id, phone_number, email_id, salary, role) VALUES
(1, 'Michael','Scott', 1, '9876543211', 'michael@dundermifflin.com', 60000, 'manager'),
(2, 'Pam','Beesly', 1, '8765432102', 'pam@dundermifflin.com', 45000, 'worker'),
(3, 'Jim','Halpert', 2, '7654321093', 'jim@dundermifflin.com', 50000, 'worker'),
(4, 'Dwight','Schrute', 3, '6543210984', 'dwight@dundermifflin.com', 55000, 'manager'),
(5, 'Angela','Martin', 4, '5432109875', 'angela@dundermifflin.com', 47000, 'worker'),
(6, 'Joshua','Snyder', 2, '865.527.5449', 'jsnyder@yahoo.com', 55979, 'manager'),
(7, 'Alicia','Boyd', 5, '320.825.7946', 'aliciaboyd@yahoo.com', 65820, 'manager'),
(8, 'Jennifer','Bentley', 1, '8859853581', 'margaret17@mullins-campos.biz', 54029, 'worker'),
(9, 'Michael','Vega', 3, '588-681-3227', 'ujohnson@hotmail.com', 52964, 'worker'),
(10, 'James','Parker', 4, '357-812-3930', 'james@dundermifflin.com', 59333, 'manager');

INSERT INTO managers(manager_id,warehouse_id,username) VALUES
(1,1,'michaelscott'),
(4,3,'dwight_schrute'),
(6,2,'joshua_snyder'),
(7,5,'alicia_boyd'),
(10,4,'james_parker');

INSERT INTO inventory(supplier_id,product_id,warehouse_id,quantity_in_stock,reorder_level) VALUES
( 1, 1, 1, 50, 10),
( 2, 2, 2, 30, 5),
( 3, 3, 3, 100, 20),
( 4, 4, 4, 75, 15),
( 5, 5, 5, 40, 8);

INSERT INTO customers (customer_id, username,first_name,last_name, age, phone_number, email_id, pincode, billing_address, shipping_address) VALUES
(1,'alice_johnson' ,'Alice','Johnson', 30, '9871234567', 'alice@mail.com', 110001, '123 Main St, NY', '456 Elm St, NY'),
(2,'bob_williams','Bob','Williams', 40, '8762345678', 'bob@mail.com', 220002, '78 Hill Rd, TX', '910 River Rd, TX'),
(3,'charlie_brown' ,'Charlie','Brown', 25, '7653456789', 'charlie@mail.com', 330003, '56 Greenway, LA', '78 Sunset Blvd, LA'),
(4,'diana_prince','Diana','Prince', 28, '6544567890', 'diana@mail.com', 440004, '99 Warrior St, SF', '12 Amazon Ave, SF'),
(5,'edward_stark','Edward','Stark', 35, '5435678901', 'edward@mail.com', 550005, '77 Ice Road, IL', '88 Castle St, IL');

INSERT INTO orders (order_id, customer_id, order_date, order_status) VALUES
(1, 1, '2025-02-15', 'On the way'),
(2, 1, '2025-02-14', 'Completed'),
(3, 1, '2025-02-13', 'On the way'),
(4, 1, '2025-02-12', 'Confirmed'),
(5, 1, '2025-02-11', 'On the way');

INSERT INTO shippings (shipping_id, delivery_date, tracking_number,shipping_status) VALUES
(1, '2025-02-18','TRK1517', 'Shipped'),
(2, '2025-02-16','TRK1518', 'Delivered'),
(3,'2025-02-15','TRK1519', 'Out for Delivery'),
(4,'2025-02-17','TRK1511', 'Processing'),
(5,'2025-02-20','TRK1512', 'In Transit'),
(6,'2025-02-27','TRK1513', 'Shipped');

INSERT INTO shipping_details (shipping_id, curr_warehouse, next_warehouse, shipping_date) VALUES
(1,1,2,'2025-02-16'),
(2,2,3,'2025-02-15'),
(3,3,2,'2025-02-11'),
(3,2,4,'2025-02-12'),
(3,4,null,'2025-02-13'),
(5,5,2,'2025-02-22'),
(5,5,2,'2025-02-23'),
(6,4,1,'2025-02-19'),
(6,1,2,'2025-02-22');

INSERT INTO order_details (order_id,shipping_id, inventory_id, quantity, amount) VALUES
(1, 1, 1, 2, 2400),
(2, 2, 2, 1, 250),
(3, 3, 3, 1, 90),
(3, 6, 4, 1, 15),
(4, 4, 4, 3, 45),
(5, 5, 5, 2, 60);

INSERT INTO procurement (inventory_id,quantity,order_date,delivery_date) VALUES
(1,2,'2025-02-16','2025-02-18'),
(2,3,'2025-02-15','2025-02-17'),
(4,2,'2025-02-11','2025-02-15'),
(4,1,'2025-02-12','2025-02-19'),
(3,5,'2025-02-16','2025-02-18');


-- username, password
-- michaelscott, micspass1
-- dwight_schrute, dwispass1
-- joshua_snyder, josspass1
-- alicia_boyd, alibpass1
-- james_parker,jamppass1
-- techworld,techpass1
-- furniture_hub,furnpass1
-- nike_suppliers,nikepass1
-- book_depot,bookpass1
-- toyland,toylpass1
-- alice_johnson,alicepass1
-- bob_williams,bobpass1
-- charlie_brown,charliepass1
-- diana_prince,dianapass1
-- edward_stark,edwardpass1


select * from order_details;
select * from procurement;
select * from warehouses;
select * from prices;
select * from products;

select * from shipping_details where shipping_id = 3;
drop function get_orders

create or replace function get_orders(id bigint default NULL , u_name varchar(150) default NULL )
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

select * from get_orders(NULL,'alice_johnson');