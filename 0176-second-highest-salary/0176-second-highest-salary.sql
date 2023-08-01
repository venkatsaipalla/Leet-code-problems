# Write your MySQL query statement below
# select ifnull(null,salary) as SecondHighestSalary from Employee
# order by salary DESC limit 1 offset 1;
select max(salary) as SecondHighestSalary from Employee 
where salary<(select max(salary) from Employee);