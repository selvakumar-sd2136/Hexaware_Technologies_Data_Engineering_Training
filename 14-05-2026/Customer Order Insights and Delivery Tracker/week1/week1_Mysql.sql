
-- CREATE DATABASE

create database CustomerOrders;

use CustomerOrders;

-- CREATE CUSTOMERS TABLE

create table customers (
    customer_id int primary key,
    customer_name varchar(100),
    region varchar(50),
    phone  varchar(15)
);

-- CREATE ORDERS TABLE

create table orders (
    order_id int primary key,
    customer_id int,
    product_name varchar(100),
    order_date date,
    delivery_date date,
    status varchar(30)
);

-- CREATE DELIVERY STATUS TABLE


create table delivery_status (
    status_id int primary key,
    order_id int,
    current_status varchar(50),
    updated_time timestamp
);

-- INSERT DATA INTO CUSTOMERS

insert into customers values(1, 'Selva', 'South', '9876543210'),(2, 'Arun', 'North', '9876543211'),
(3, 'Priya', 'West', '9876543212');


-- INSERT DATA INTO ORDERS


insert into orders values(101, 1, 'Laptop', '2026-05-01', '2026-05-10', 'Delivered'),(102, 1, 'Mouse', '2026-05-03', '2026-05-05', 'Delivered'),
(103, 2, 'Keyboard', '2026-05-02', '2026-05-12', 'Delayed'),(104, 3, 'Mobile', '2026-05-04', '2026-05-06', 'Delivered');

-- INSERT DATA INTO DELIVERY STATUS

insert into delivery_status values(1, 101, 'Delivered', NOW()),(2, 102, 'Delivered', NOW()),
(3, 103, 'Delayed', NOW()),(4, 104, 'Out For Delivery', NOW());


-- CRUD OPERATIONS


-- READ
select * from orders;

-- UPDATE
update orders
set status = 'Delivered'
where order_id = 103;

select * from orders;

-- DELETE
delete from orders
where order_id = 104;

select * from orders;

-- STORED PROCEDURE
-- FETCH DELAYED DELIVERIES

DELIMITER //

create procedure GetDelayedOrders(in cust_id int)
begin
    select * from orders
    where customer_id = cust_id and delivery_date > DATE_ADD(order_date, INTERVAL 5 DAY);
end //

DELIMITER ;

-- CALL STORED PROCEDURE

call GetDelayedOrders(1);

-- VIEW TABLES

 select * from customers;

select * from orders;

select * from delivery_status;