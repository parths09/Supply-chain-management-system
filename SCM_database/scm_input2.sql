
delete from products;
INSERT INTO products (product_id, name, description, category) VALUES
(1, 'Organic Almonds', 'Raw, unsalted almonds grown organically. High in protein and healthy fats.', 'Nuts'),
(2, 'Italian Extra Virgin Olive Oil', 'Cold-pressed olive oil from Italy, rich in antioxidants and perfect for cooking and dressing.', 'Cooking Oil'),
(3, 'Stainless Steel Water Bottle', 'Eco-friendly, reusable 500ml stainless steel water bottle. Keeps drinks cold for 12 hours.', 'Drinkware'),
(4, 'Himalayan Pink Salt', 'Natural pink salt harvested from the Himalayan mountains. Adds a unique flavor to your dishes.', 'Seasoning'),
(5, 'Gluten-Free Spaghetti', 'A premium gluten-free pasta made with rice and corn flour, perfect for gluten-sensitive diets.', 'Pasta'),
(6, 'Electric Standing Desk', 'Adjustable standing desk with motorized height settings, designed for ergonomic office work.', 'Office Furniture'),
(7, 'Aromatherapy Diffuser', 'Ultrasonic diffuser with LED lights, ideal for creating a calming atmosphere in any room.', 'Home Decor'),
(8, 'Vegan Protein Powder', 'Plant-based protein powder made from peas and brown rice, ideal for muscle recovery.', 'Health Supplements'),
(9, 'Leather Office Chair', 'Executive office chair with high-back design and leather upholstery for comfort and style.', 'Office Furniture'),
(10, 'Bamboo Toothbrush', 'Eco-friendly toothbrush made from sustainable bamboo, soft bristles for gentle cleaning.', 'Personal Care'),
(11, 'Organic Green Tea', 'Pure organic green tea leaves, known for their antioxidants and health benefits.', 'Beverages'),
(12, 'Wireless Noise Cancelling Headphones', 'Over-ear headphones with active noise cancellation, providing clear sound and comfort.', 'Electronics'),
(13, 'Ceramic Nonstick Cookware Set', '5-piece cookware set with ceramic coating, free from harmful chemicals.', 'Kitchenware'),
(14, 'Handcrafted Wooden Cutting Board', 'Durable, handmade cutting board crafted from sustainable hardwood.', 'Kitchenware'),
(15, 'Natural Honey', 'Raw honey harvested from local beekeepers, known for its natural sweetness and health benefits.', 'Sweeteners'),
(16, 'Memory Foam Mattress', 'High-quality memory foam mattress designed for optimal comfort and support.', 'Furniture'),
(17, 'Indoor Potted Plant', 'Low-maintenance houseplant, perfect for indoor spaces to improve air quality and decor.', 'Home Decor'),
(18, 'Solar-Powered Outdoor Lantern', 'Energy-efficient outdoor lantern powered by solar panels, ideal for garden lighting.', 'Outdoor Lighting'),
(19, 'Electric Coffee Grinder', 'Electric grinder for fresh coffee beans, with adjustable grind settings.', 'Kitchen Appliances'),
(20, 'Yoga Mat', 'Non-slip, eco-friendly yoga mat with extra thickness for comfort during practice.', 'Fitness Gear');


delete from suppliers;
INSERT INTO suppliers (supplier_id, supplier_name, phone_number, email_id, address, pincode, username) VALUES
(1, 'NutriHarvest Foods', '9876543210', 'contact@nutriharvest.com', '12 Orchard Street, Pune', '411001', 'nutriharvest'),
(2, 'CasaCraft Living', '9345678123', 'support@casacraft.in', '55 Woodfield Estate, Kochi', '682030', 'casacraft'),
	(3, 'GreenGlow Wellness', '9988776655', 'hello@greenglow.com', '88 Muscle Avenue, Hyderabad', '500081', 'greenglow'),
(4, 'OfficePro Solutions', '9785612345', 'sales@officepro.com', '1st Floor, Tower A, Gurugram', '122001', 'officepro'),
(5, 'BrewPro Kitchenware', '9812345670', 'orders@brewpro.com', '77 Roastery Blvd, Mumbai', '400001', 'brewpro');


delete from prices;
INSERT INTO prices (product_id, supplier_id, unit_price, active) VALUES
-- NutriHarvest Foods
(1, 1, 450.00, TRUE),
(2, 1, 850.00, TRUE),
(4, 1, 120.00, TRUE),
(5, 1, 275.00, TRUE),
(11, 1, 300.00, TRUE),
(15, 1, 400.00, TRUE),

-- CasaCraft Living
(6, 2, 15500.00, TRUE),
(9, 2, 9800.00, TRUE),
(14, 2, 950.00, TRUE),
(16, 2, 18000.00, TRUE),
(17, 2, 650.00, TRUE),
(18, 2, 1100.00, TRUE),

-- GreenGlow Wellness
(7, 3, 1400.00, TRUE),
(8, 3, 2200.00, TRUE),
(10, 3, 120.00, TRUE),
(20, 3, 999.00, TRUE),

-- OfficePro Solutions
(3, 4, 750.00, TRUE),
(12, 4, 5990.00, TRUE),

-- BrewPro Kitchenware
(13, 5, 3400.00, TRUE),
(19, 5, 1850.00, TRUE);


delete from warehouses;
INSERT INTO warehouses (warehouse_id, name, location, phone_number, pincode) VALUES
(1, 'North Hub Warehouse', 'Delhi', '01123456789', '110001'),
(2, 'Western Logistics Depot', 'Mumbai', '02234567890', '400001'),
(3, 'Eastern Storage Point', 'Kolkata', '03345678901', '700001'),
(4, 'Southern Distribution Center', 'Chennai', '04456789012', '600001'),
(5, 'Central Fulfillment Hub', 'Nagpur', '07126789012', '440001');


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

delete from inventory;
INSERT INTO inventory(supplier_id,product_id,warehouse_id,quantity_in_stock,reorder_level) VALUES
-- NutriHarvest Foods
( 1, 1, 1, 50, 10),
(1, 1, 1, 120, 30),
(1, 2, 2, 80, 20),
(1, 4, 3, 200, 50),
(1, 5, 4, 150, 40),
(1, 11, 5, 100, 25),
-- CasaCraft Living
(2, 6, 1, 20, 5),
(2, 9, 2, 18, 5),
(2, 14, 3, 35, 10),
(2, 16, 4, 10, 3),
(2, 17, 5, 50, 10),
-- GreenGlow Wellness
(3, 7, 1, 60, 15),
(3, 8, 2, 70, 20),
(3, 10, 3, 200, 50),
(3, 20, 4, 100, 25),
-- OfficePro Solutions
(4, 3, 1, 150, 30),
(4, 3, 4, 140, 30),
(4, 12, 5, 25, 5),
-- BrewPro Kitchenware
(5, 13, 1, 30, 10),
(5, 13, 2, 30, 10),
(5, 19, 2, 40, 10);

INSERT INTO customers (customer_id, username,first_name,last_name, age, phone_number, email_id, pincode, billing_address, shipping_address) VALUES
(1,'alice_johnson' ,'Alice','Johnson', 30, '9871234567', 'alice@mail.com', 110001, '123 Main St, NY', '456 Elm St, NY'),
(2,'bob_williams','Bob','Williams', 40, '8762345678', 'bob@mail.com', 220002, '78 Hill Rd, TX', '910 River Rd, TX'),
(3,'charlie_brown' ,'Charlie','Brown', 25, '7653456789', 'charlie@mail.com', 330003, '56 Greenway, LA', '78 Sunset Blvd, LA'),
(4,'diana_prince','Diana','Prince', 28, '6544567890', 'diana@mail.com', 440004, '99 Warrior St, SF', '12 Amazon Ave, SF'),
(5,'edward_stark','Edward','Stark', 35, '5435678901', 'edward@mail.com', 550005, '77 Ice Road, IL', '88 Castle St, IL');

-- delete from procurements
-- INSERT INTO procurements (inventory_id,quantity,order_date,delivery_date,status) VALUES
-- (1,2,'2025-02-16','2025-02-18','Processing'),
-- (6,100,'2025-02-16','2025-02-18','In transit'),
-- (2,3,'2025-02-12','2025-02-14','Delivered'),
-- (4,2,'2025-02-11','2025-02-17','In transit'),
-- (4,1,'2025-02-12','2025-02-15','Delivered'),
-- (3,5,'2025-02-16','2025-02-18','Processing');


-- username, password
-- michaelscott, micspass1
-- dwight_schrute, dwispass1
-- joshua_snyder, josspass1
-- alicia_boyd, alibpass1
-- james_parker,jamppass1
-- nutriharvest,nutripass1
-- casacraft,casapass1
-- greenglow, greenpass1
-- officepro,offpass1
-- brewpro,brewpass1
-- alice_johnson,alicepass1
-- bob_williams,bobpass1
-- charlie_brown,charliepass1
-- diana_prince,dianapass1
-- edward_stark,edwardpass1

