--product table
drop table if exists products cascade; --drop .. cascade drops the constraints in this case

create table products (
product_id bigint primary key,
name varchar(50) not null,
description text,
category text
);

--Supplier table
drop table if exists suppliers cascade; 

create table suppliers(
supplier_id bigint primary key,
username varchar(150) not null,
supplier_name varchar(150) not null,
phone_number varchar(15) not null unique,
email_id varchar(30) not null unique,
address text,
pincode int not null
);

--prices table
drop table if exists prices;

create table prices(
product_id bigint,
supplier_id bigint ,
unit_price numeric(10,2) not null check(unit_price > 0),
active boolean,
foreign key (product_id) references products(product_id) on delete cascade,
foreign key (supplier_id) references suppliers(supplier_id) on delete cascade
);


--Customer table
drop table if exists customers cascade;

create table customers
(
customer_id bigint primary key,
username varchar(150) not null,
first_name varchar(150) not null,
last_name varchar(150) not null,
age smallint not null check(age>=18),
phone_number varchar(15) not null unique,
email_id varchar(30) not null unique,
pincode int not null,
billing_address text,
shipping_address text
);


--warehouses table
drop table if exists warehouses cascade;

create table warehouses(
warehouse_id int primary key,
name varchar(50) not null,
location varchar(255),
phone_number varchar(15) unique,
pincode int not null
);


--employee table
drop table if exists employees cascade;

create table employees(
employee_id bigint primary key,
first_name varchar(150) not null,
last_name varchar(150) not null,
warehouse_id bigint not null,
phone_number varchar(15) not null unique,
email_id varchar(50) not null unique,
salary numeric(10,2),
role varchar(20) not null check (role in ('worker', 'manager')),
foreign key (warehouse_id) references warehouses(warehouse_id) on delete set null -- say the wh is closed, but we can still relocate the employees to diff wh
);


--manager table
drop table if exists managers cascade;

create table managers(
manager_id bigint primary key,
warehouse_id bigint not null,
username varchar(150),
foreign key (manager_id) references employees(employee_id) on delete set null,
foreign key (warehouse_id) references warehouses(warehouse_id) on delete cascade,
foreign key (username) references auth_user(username) on delete set null
);


--inventory table
drop table if exists inventory cascade;

create table inventory(
inventory_id serial primary key,
product_id bigint not null,
supplier_id bigint not null,
warehouse_id int not null,
quantity_in_stock int not null check(quantity_in_stock>=0),
reorder_level int,
alert boolean default true not null,
foreign key (product_id) references products(product_id) on delete restrict,
foreign key (supplier_id) references suppliers(supplier_id) on delete restrict,
foreign key (warehouse_id) references warehouses(warehouse_id) on delete restrict
);

alter table inventory add alert boolean default true not null;

--procurement table
drop table if exists procurement;

create table procurement(
procurement_id serial primary key,
inventory_id bigint not null,
quantity int not null,
order_date date not null,
delivery_date date not null, --delivery date > order date
status varchar(20) default 'Processing' not null check (status in ('Delivered','In transit','Processing')),
foreign key (inventory_id) references inventory(inventory_id) on delete cascade --you dont want to erase 
);

--orders table
drop table if exists orders cascade;

create table orders(
order_id bigint primary key,
customer_id bigint not null,
order_date date not null,
total_amount numeric(10,2),
order_status varchar(15) default 'pending' not null check(order_status in ('Pending','Confirmed','On the way','Completed')),
foreign key (customer_id) references customers(customer_id) on delete cascade
);

--shippings table
drop table if exists shippings cascade;

create table shippings(
shipping_id bigint primary key,
delivery_date date,
tracking_number varchar(15) not null,
shipping_status varchar(20) default 'Pending' not null check(shipping_status in ('Pending',  'Processing', 'Shipped','In Transit', 'Out for Delivery', 'Delivered'))
);
--shipping_details
drop table if exists shipping_details cascade;

create table shipping_details(
detail_id serial primary key,
shipping_id bigint not null,
shipping_date date,
curr_warehouse int not null,
next_warehouse int,
foreign key (curr_warehouse) references warehouses(warehouse_id),
foreign key (next_warehouse) references warehouses(warehouse_id),
foreign key (shipping_id ) references shippings (shipping_id)
);


--order_details table
drop table if exists order_details;

create table order_details(
detail_id serial primary key,
order_id bigint not null,
inventory_id bigint not null,
shipping_id bigint not null,
quantity int not null check(quantity>0),
amount numeric(10,2) check(amount>0),
foreign key (order_id) references orders(order_id) on delete restrict,
foreign key (inventory_id) references inventory(inventory_id) on delete restrict,
foreign key (shipping_id) references shippings(shipping_id) on delete restrict
);

drop table if exists requests;

create table requests(
request_id serial primary key,
product_id bigint not null,
supplier_id bigint not null,
warehouse_id integer not null,
quantity integer not null,
contact_email varchar(50),
unit_price numeric(10,2) not null,
approval varchar(20) default 'Pending' check (approval in ('Pending','Accepted','Denied')) not null,
foreign key (product_id) references products(product_id) on delete cascade,
foreign key (supplier_id) references suppliers(supplier_id) on delete cascade,
foreign key (warehouse_id) references warehouses(warehouse_id) on delete cascade
);















