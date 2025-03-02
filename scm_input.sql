
INSERT INTO products (product_id, name, description, category) VALUES
(1, 'Laptop', '15-inch, Intel i7, 16GB RAM', 'Electronics'),
(2, 'Office Chair', 'Ergonomic chair with lumbar support', 'Furniture'),
(3, 'Running Shoes', 'Lightweight with cushioned sole', 'Clothing'),
(4, 'Fiction Book', 'Bestselling novel', 'Books'),
(5, 'Teddy Bear', 'Soft plush toy for kids', 'Toys');

INSERT INTO suppliers (supplier_id, name, phone_number, email_id, address, pincode, password) VALUES
(1, 'TechWorld Ltd.', '9876543210', 'contact@techworld.com', '123 Tech Street, NY', 10001, 'pass123'),
(2, 'Furniture Hub', '9123456789', 'support@furnihub.com', '456 Wood Ave, LA', 90001, 'chair789'),
(3, 'Nike Suppliers', '9988776655', 'nike@shoes.com', '789 Sport Lane, TX', 73301, 'runfast!'),
(4, 'BookDepot', '8765432109', 'info@bookdepot.com', '101 Reading Blvd, SF', 94101, 'readmore'),
(5, 'ToyLand Inc.', '7553311223', 'hello@toyland.com', '202 Happy St, FL', 33101, 'fun4kids');

INSERT INTO prices (product_id, supplier_id, unit_price) VALUES
(1, 1, 1200.00),
(2, 2, 250.00),
(3, 3, 90.00),
(4, 4, 15.00),
(5, 5, 30.00);

--inserting manager into warehouse is little complicated

INSERT INTO warehouses (warehouse_id, name, location, phone_number, manager_id, pincode) VALUES
(1, 'Warehouse A', 'New York', '9876543211', null, 10001),
(2, 'Warehouse B', 'Los Angeles', '8765432102', null, 90001),
(3, 'Warehouse C', 'Texas', '7654321093', null, 73301),
(4, 'Warehouse D', 'San Francisco', '6543210984', null, 94101),
(5, 'Warehouse E', 'Florida', '5432109875', null, 33101);

INSERT INTO employees (employee_id, name, warehouse_id, phone_number, email_id, salary, password, role) VALUES
(1, 'Michael Scott', 1, '9876543211', 'michael@dundermifflin.com', 60000, 'worldsbestboss', 'manager'),
(2, 'Pam Beesly', 1, '8765432102', 'pam@dundermifflin.com', 45000, 'artsales', 'worker'),
(3, 'Jim Halpert', 2, '7654321093', 'jim@dundermifflin.com', 50000, 'prankster', 'worker'),
(4, 'Dwight Schrute', 3, '6543210984', 'dwight@dundermifflin.com', 55000, 'bearsbeets', 'manager'),
(5, 'Angela Martin', 4, '5432109875', 'angela@dundermifflin.com', 47000, 'catsrule', 'worker'),
(6, 'Joshua Snyder', 2, '865.527.5449', 'sroberts@yahoo.com', 55979, 'within', 'manager'),
(7, 'Alicia Boyd', 5, '320.825.7946', 'katherinewalters@yahoo.com', 65820, 'shoulder', 'manager'),
(8, 'Jennifer Bentley', 1, '8859853581', 'margaret17@mullins-campos.biz', 54029, 'almost', 'worker'),
(9, 'Michael Vega', 3, '588-681-3227', 'ujohnson@hotmail.com', 52964, 'speech', 'worker'),
(10, 'James Parker', 4, '357-812-3930', 'dawn57@casey.biz', 59333, 'million', 'manager');

update warehouses
set manager_id = (select e.employee_id from employees e where e.warehouse_id = warehouses.warehouse_id and e.role = 'manager' );

INSERT INTO inventory(supplier_id,product_id,warehouse_id,quantity_in_stock,reorder_level) VALUES
( 1, 1, 1, 50, 10),
( 2, 2, 2, 30, 5),
( 3, 3, 3, 100, 20),
( 4, 4, 4, 75, 15),
( 5, 5, 5, 40, 8);

INSERT INTO customers (customer_id, name, age, phone_number, email_id, pincode, billing_address, shipping_address, password) VALUES
(1, 'Alice Johnson', 30, '9871234567', 'alice@mail.com', 110001, '123 Main St, NY', '456 Elm St, NY', 'alicepass'),
(2, 'Bob Williams', 40, '8762345678', 'bob@mail.com', 220002, '78 Hill Rd, TX', '910 River Rd, TX', 'bobsecure'),
(3, 'Charlie Brown', 25, '7653456789', 'charlie@mail.com', 330003, '56 Greenway, LA', '78 Sunset Blvd, LA', 'charlie321'),
(4, 'Diana Prince', 28, '6544567890', 'diana@mail.com', 440004, '99 Warrior St, SF', '12 Amazon Ave, SF', 'wonderwoman'),
(5, 'Edward Stark', 35, '5435678901', 'edward@mail.com', 550005, '77 Ice Road, IL', '88 Castle St, IL', 'winteriscoming');

INSERT INTO orders (order_id, customer_id, order_date, order_status) VALUES
(1, 1, '2025-02-15', 'on the way'),
(2, 1, '2025-02-14', 'completed'),
(3, 3, '2025-02-13', 'on the way'),
(4, 4, '2025-02-12', 'confirmed'),
(5, 5, '2025-02-11', 'completed');

INSERT INTO shippings (shipping_id, delivery_date, tracking_number,shipping_status) VALUES
(1, '2025-02-18','TRK1517', 'shipped'),
(2, '2025-02-16','TRK1518', 'delivered'),
(3,'2025-02-15','TRK1519', 'out for delivery'),
(4,'2025-02-17','TRK1511', 'processing'),
(5,'2025-02-20','TRK1512', 'cancelled'),
(6,'2025-02-17','TRK1513', 'shipped');

INSERT INTO shipping_details (shipping_id, curr_warehouse, next_warehouse, shipping_date) VALUES
(1,1,2,'2025-02-16'),
(2,2,3,'2025-02-15'),
(3,3,2,'2025-02-11'),
(3,2,4,'2025-02-11'),
(3,4,null,'2025-02-11'),
(4,4,1,'2025-02-12'),
(5,5,2,'2025-02-16'),
(6,4,1,'2025-02-12'),
(6,1,2,'2025-02-12');

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



select * from order_details;
select * from procurement;
select * from warehouses;

select * from shipping_details where shipping_id = 3;

