CREATE DATABASE company_training;

use company_training;

CREATE TABLE employees (
 emp_id INT PRIMARY KEY,
 emp_name VARCHAR(100),
 department VARCHAR(50),
 city VARCHAR(50)
);

CREATE TABLE projects (
 project_id INT PRIMARY KEY,
 emp_id INT,
 project_name VARCHAR(100),
 project_budget DECIMAL(12,2),
 project_status VARCHAR(50)
);

INSERT INTO employees VALUES
(1, 'Rohan Mehta', 'IT', 'Hyderabad'),
(2, 'Sneha Iyer', 'IT', 'Bangalore'),
(3, 'Kiran Patel', 'Finance', 'Mumbai'),
(4, 'Ananya Das', 'HR', NULL),
(5, 'Rahul Sharma', 'IT', 'Delhi'),
(6, NULL, 'Marketing', 'Chennai');

INSERT INTO projects VALUES
(101, 1, 'AI Chatbot', 120000, 'Active'),
(102, 1, 'ML Prediction', 90000, 'Active'),
(103, 2, 'Data Warehouse', 150000, 'Active'),
(104, 3, 'Financial Dashboard', 80000, 'Completed'),
(105, NULL, 'Website Revamp', 60000, 'Pending'),
(106, 8, 'Mobile App', 100000, 'Active');

select * from employees;
select * from projects;

-- File 1
-- exercise 1

select e.emp_name,p.project_name,p.project_budget from employees as e 
inner join projects as p on e.emp_id=p.emp_id;

-- exercise 2

select e.emp_name,p.project_name from employees as e 
left join projects as p on e.emp_id=p.emp_id;


-- exercise 3

select e.emp_name, p.project_name from projects as p
left join employees as e on e.emp_id = p.emp_id;

-- exercise 4 

select e.emp_name, p.project_name from employees as e
left join projects as p on e.emp_id = p.emp_id
union
select e.emp_name, p.project_name from employees as e 
right join projects as p on e.emp_id = p.emp_id;

-- exercise 5

select e.emp_name, p.project_name from employees as e
cross join projects as p;

-- exercise 6

select p.project_name from projects as p 
inner join employees as e on e.emp_id=p.emp_id where e.department='IT';

-- exercise 7

select project_name,project_budget from projects  
where project_budget>100000;

-- exercise 8

select e.emp_name,e.city,p.project_name from employees as e
inner join projects as p on e.emp_id=p.emp_id where e.city='Hyderabad';

-- exercise 9

select e.emp_name,count(p.project_name) as Total_projects from employees as e 
left join projects as p on e.emp_id=p.emp_id group by e.emp_id,e.emp_name;

-- exercise 10

select e.emp_name,sum(p.project_budget) as Total_project_budgets from employees as e 
left join projects as p on e.emp_id=p.emp_id group by e.emp_id;

-- exercise 11

select e.department,avg(p.project_budget)as Average_budget from employees as e 
left join projects as p on e.emp_id=p.emp_id group by e.department;

-- exercise 12

select e.department,count(p.project_name) as Total_projects from employees as e 
left join projects as p on e.emp_id=p.emp_id group by e.department;

-- exercise 13

select e.department,sum(p.project_budget) as Total_budgets from employees as e 
left join projects as p on e.emp_id=p.emp_id group by e.department;

-- exercise 14

select e.city,count(e.emp_name) as Number_of_employees from Employees as e 
left join projects as p on e.emp_id=p.emp_id group by e.city;

-- exercise 15

select e.emp_name,count(p.project_name) as Total_projects from Employees as e 
join projects as p on e.emp_id=p.emp_id group by e.emp_id having(count(p.project_name))>1;

-- exercise 16

select e.department,sum(p.project_budget) as Total_budgets from employees as e
join projects as p on p.emp_id=e.emp_id group by e.department having(Total_budgets)>150000; 

-- exercise 17

select e.emp_name,sum(p.project_budget) as Total_budgets from employees as e
join projects as p on p.emp_id=e.emp_id group by e.emp_id having(sum(p.project_budget))>100000;

-- capstone query

select e.emp_name,e.department,sum(p.project_budget) as Total_project_budget from employees as e 
join projects as p on e.emp_id=p.emp_id group by e.emp_id having(sum(p.project_budget) )>100000 order by sum(p.project_budget) desc;

