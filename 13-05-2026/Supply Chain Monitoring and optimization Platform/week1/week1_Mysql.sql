-- Create Database
create database supply_chain;
use supply_chain;

-- CRUD OPERATIONS

-- create orders table
create table orders(
    order_id int primary key,
    supplier_id int,
    product_name varchar(100),
    quantity int,
    order_date date,
    delivery_date date
);

-- create suppliers table
create table suppliers(
    supplier_id int primary key,
    supplier_name varchar(100),
    location varchar(100)
);

-- create inventory table
create table inventory(
    product_id int primary key,
    product_name varchar(100),
    stock int
);

-- Inserting datas for all the tables

insert into orders values
(101,1,'Laptop',5,'2026-01-01','2026-01-05'),
(102,2,'Mouse',20,'2026-01-02','2026-01-10'),
(103,1,'Keyboard',10,'2026-01-03','2026-01-04');

insert into suppliers values
(1,'Dell','Chennai'),
(2,'HP','Bangalore');

insert into inventory values
(1,'Laptop',8),
(2,'Mouse',100),
(3,'Keyboard',15);


-- Read (select)
select * from orders;
select * from suppliers;
select * from inventory;

-- Update
update inventory
set stock=20
where product_id=1;

select * from inventory;

-- delete
delete from orders
where order_id=103;

select * from orders;

-- Stored Procedure
DELIMITER //

create procedure low_stock_product()
begin
    select * from inventory
    where stock >10;
end //

DELIMITER ;

call low_stock_product();