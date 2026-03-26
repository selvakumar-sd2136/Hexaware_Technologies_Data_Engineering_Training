CREATE DATABASE capstone_sql;
USE capstone_sql;

CREATE TABLE students (
 student_id INT PRIMARY KEY,
 student_name VARCHAR(100),
 city VARCHAR(50),
 age INT
);

CREATE TABLE enrollments (
 enrollment_id INT PRIMARY KEY,
 student_id INT,
 course_name VARCHAR(100),
 trainer VARCHAR(100),
 fee DECIMAL(10,2)
);

INSERT INTO students VALUES
(1,'Aarav Sharma','Hyderabad',22),
(2,'Priya Reddy','Bangalore',23),
(3,'Rahul Verma','Mumbai',24),
(4,'Sneha Kapoor',NULL,21),
(5,'Vikram Singh','Chennai',25),
(6,NULL,'Delhi',22);

INSERT INTO enrollments VALUES
(101,1,'MySQL','Abdullah Khan',5000),
(102,1,'Python','Abdullah Khan',7000),
(103,2,'Power BI','Kiran',6000),
(104,3,'Azure Data Factory','Sneha',8000),
(105,NULL,'Excel','Rohan',3000),
(106,8,'Databricks','Ananya',9000);


select * from students;
select * from enrollments;

-- File 2

-- exercise 1 
select s.student_name,e.course_name from students as s 
inner join enrollments as e on s.student_id=e.student_id;

-- exercise 2
select s.student_name,e.course_name from students as s 
left join enrollments as e on s.student_id=e.student_id;

-- exercise 3
select s.student_name,e.course_name from enrollments as e
left join students as s on s.student_id=e.student_id;

-- exercise 4 

select s.student_name,e.course_name from students as s 
left join enrollments as e on s.student_id=e.student_id
union
select s.student_name,e.course_name from enrollments as e
left join students as s on s.student_id=e.student_id;

-- exercise 5
select s.student_name, e.course_name from students as s
cross join enrollments as e;

-- exercise 6
select s.student_name,e.course_name,s.city from students as s
join enrollments as e on s.student_id=e.student_id where s.city='Hyderabad';

-- exercise 7 
select course_name,fee from enrollments where fee>6000;

-- exercise 8
select s.student_name,count(e.enrollment_id) as Total_courses from students as s 
left join enrollments as e on s.student_id=e.student_id group by s.student_id,s.student_name;

-- exercise 9 
select s.student_name,sum(e.fee) as Total_fees from students as s 
left join enrollments as e on s.student_id=e.student_id group by s.student_id,s.student_name;

-- exercise 10
select s.student_name,count(e.enrollment_id) as Total_courses from students as s 
join enrollments as e on s.student_id=e.student_id group by s.student_id having count(e.enrollment_id)>1;

-- exercise 11

select trainer,sum(fee) as collected_fees from enrollments 
group by trainer having sum(fee)>10000;

-- exercise 12
select city,count(student_id) as Total_students from students 
group by city having count(student_id)>1;

-- capstone

select s.student_name,s.city,sum(e.fee) as Total_fees from students as s 
join enrollments as e on e.student_id=s.student_id group by s.student_id having(sum(e.fee)>5000) 
order by Total_fees desc;

