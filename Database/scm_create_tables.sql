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
name varchar(50) not null,
phone_number varchar(15) not null unique,
email_id varchar(30) not null unique,
address text,
pincode int not null,
password varchar(30) not null
);

--prices table
drop table if exists prices;

create table prices(
product_id bigint,
supplier_id bigint ,
unit_price numeric(10,2) not null check(unit_price > 0),
foreign key (product_id) references products(product_id) on delete cascade,
foreign key (supplier_id) references suppliers(supplier_id) on delete cascade
);


--Customer table
drop table if exists customers cascade;

create table customers
(
customer_id bigint primary key,
name varchar(30) not null,
age smallint not null check(age>=18),
phone_number varchar(15) not null unique,
email_id varchar(30) not null unique,
pincode int not null,
billing_address text,
shipping_address text,
password varchar(30) not null
);


--warehouses table
drop table if exists warehouses cascade;

create table warehouses(
warehouse_id int primary key,
name varchar(50) not null,
location varchar(255),
phone_number varchar(15) unique,
manager_id bigint,
pincode int not null
);


--employee table
drop table if exists employees cascade;

create table employees(
employee_id bigint primary key,
name varchar(50) not null,
warehouse_id bigint not null,
phone_number varchar(15) not null unique,
email_id varchar(50) not null unique,
salary numeric(10,2),
password varchar(30),
role varchar(20) not null check (role in ('worker', 'manager')),
foreign key (warehouse_id) references warehouses(warehouse_id) on delete set null -- say the wh is closed, but we can still relocate the employees to diff wh
);


--setting foreign key constraints in warehouse table
alter table warehouses 
add constraint FK_warehouse_manager 
foreign key (manager_id) references employees(employee_id) on delete set null;


--inventory table
drop table if exists inventory cascade;

create table inventory(
inventory_id serial primary key,
product_id bigint not null,
supplier_id bigint not null,
warehouse_id int not null,
quantity_in_stock int not null check(quantity_in_stock>=0),
reorder_level int,
foreign key (product_id) references products(product_id) on delete restrict,
foreign key (supplier_id) references suppliers(supplier_id) on delete restrict,
foreign key (warehouse_id) references warehouses(warehouse_id) on delete restrict
);

--procurement table
drop table if exists procurement;

create table procurement(
procurement_id serial primary key,
inventory_id bigint not null	,
quantity int not null,
order_date date not null,
delivery_date date not null, --delivery date > order date
foreign key (inventory_id) references inventory(inventory_id) on delete cascade --you dont want to erase 
);

--orders table
drop table if exists orders cascade;

create table orders(
order_id bigint primary key,
customer_id bigint not null,
order_date date not null,
total_amount numeric(10,2),
order_status varchar(15) default 'pending' not null check(order_status in ('pending','confirmed','on the way','completed')),
foreign key (customer_id) references customers(customer_id) on delete cascade
);

--shippings table
drop table if exists shippings cascade;

create table shippings(
shipping_id bigint primary key,
delivery_date date,
tracking_number varchar(15) not null,
shipping_status varchar(20) default 'pending' not null check(shipping_status in ('pending',  'processing', 'shipped','in transit', 'out for delivery', 'delivered', 'cancelled'))
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





















