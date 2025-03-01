insert into products(product_id,product_name,category) values
(1,'a','aa'),(2,'b','bb'),(3,'c','cc');

insert into suppliers(supplier_id,supplier_name) values
(1,'x'),(2,'y');

insert into prices(product_id,supplier_id,price) values
(1,1,100.12),(1,2,110.00),(2,1,2000),(3,2,1000);

select * from products;
select * from suppliers;
select * from prices

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

INSERT INTO warehouses (warehouse_id, name, location, phone_number, manager_id, pincode) VALUES
(1, 'Tech Warehouse A', 'New York', '9876543211', 1, 10001),
(2, 'Furniture Depot', 'Los Angeles', '8765432102', 6, 90001),
(3, 'Shoe Storage', 'Texas', '7654321093', 4, 73301),
(4, 'Book Warehouse', 'San Francisco', '6543210984', 10, 94101),
(5, 'Toy Distribution Center', 'Florida', '5432109875', 7, 33101);

INSERT INTO employees (employee_id, name, warehouse_id, phone_number, email_id, salary, password, role) VALUES
(1, 'Michael Scott', 1, '9876543211', 'michael@dundermifflin.com', 60000, 'worldsbestboss', 'manager'),
(2, 'Pam Beesly', 1, '8765432102', 'pam@dundermifflin.com', 45000, 'artsales', 'worker'),
(3, 'Jim Halpert', 2, '7654321093', 'jim@dundermifflin.com', 50000, 'prankster', 'worker'),
(4, 'Dwight Schrute', 3, '6543210984', 'dwight@dundermifflin.com', 55000, 'bearsbeets', 'manager'),
(5, 'Angela Martin', 4, '5432109875', 'angela@dundermifflin.com', 47000, 'catsrule', 'worker');
(6, 'Joshua Snyder', 2, '865.527.5449', 'sroberts@yahoo.com', 55979, 'within', 'manager'),
(7, 'Alicia Boyd', 5, '320.825.7946', 'katherinewalters@yahoo.com', 65820, 'shoulder', 'manager'),
(8, 'Jennifer Bentley', 1, '8859853581', 'margaret17@mullins-campos.biz', 54029, 'almost', 'manager'),
(9, 'Michael Vega', 3, '588-681-3227', 'ujohnson@hotmail.com', 52964, 'speech', 'worker'),
(10, 'James Parker', 4, '357-812-3930', 'dawn57@casey.biz', 59333, 'million', 'manager');


INSERT INTO inventory(inventory_id,supplier_id,product_id,warehouse_id,quantity_in_stock,reorder_level) VALUES
(1, 1, 1, 1, 50, 10),
(2, 2, 2, 2, 30, 5),
(3, 3, 3, 3, 100, 20),
(4, 4, 4, 4, 75, 15),
(5, 5, 5, 5, 40, 8);

INSERT INTO customers (customer_id, name, age, phone_number, email_id, pincode, billing_address, shipping_address, password) VALUES
(1, 'Alice Johnson', 30, '9871234567', 'alice@mail.com', 110001, '123 Main St, NY', '456 Elm St, NY', 'alicepass'),
(2, 'Bob Williams', 40, '8762345678', 'bob@mail.com', 220002, '78 Hill Rd, TX', '910 River Rd, TX', 'bobsecure'),
(3, 'Charlie Brown', 25, '7653456789', 'charlie@mail.com', 330003, '56 Greenway, LA', '78 Sunset Blvd, LA', 'charlie321'),
(4, 'Diana Prince', 28, '6544567890', 'diana@mail.com', 440004, '99 Warrior St, SF', '12 Amazon Ave, SF', 'wonderwoman'),
(5, 'Edward Stark', 35, '5435678901', 'edward@mail.com', 550005, '77 Ice Road, IL', '88 Castle St, IL', 'winteriscoming');

INSERT INTO orders (Order_id, Customer_id, Order_date, Status) VALUES
(1, 1, '2025-02-15', 'on the way'),
(2, 1, '2025-02-14', 'completed'),
(3, 1, '2025-02-13', 'on the way'),
(4, 1, '2025-02-12', 'confirmed'),
(5, 1, '2025-02-11', 'completed');

INSERT INTO shipments (shipment_id, warehouse_id, shipping_date, delivery_date, status, location) VALUES
(1, 1, '2025-02-16','2025-02-18', 'shipped',),
(2, 2, '2025-02-15','2025-02-16', 'delivered',),
(3, 3, '2025-02-14','2025-02-16', 'out for delivery',),
(4, 4, '2025-02-13','2025-02-16', 'processing',),
(5, 5, '2025-02-12','2025-02-16', 'Cancelled',);

INSERT INTO order_details (order_id,shipment_id, inventory_id, quantity, amount) VALUES
(1, 1, 1, 2, 2400),
(2, 2, 2, 1, 250),
(3, 3, 3, 1, 90),
(4, 4, 4, 3, 45),
(5, 5, 5, 2, 60);







