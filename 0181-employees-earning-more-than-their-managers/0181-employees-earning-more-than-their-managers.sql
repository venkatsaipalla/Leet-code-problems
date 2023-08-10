# Write your MySQL query statement below

# with Temp as (

# select * from Employee
# )


# select distinct Temp.name as Employee from Temp 
# inner join Employee on Temp.id=Employee.managerId
# where Temp.salary<Employee.salary

select e2.name as Employee from Employee e1
inner join Employee e2 on e1.id=e2.managerId
where e2.salary>e1.salary


# SELECT
#      a.NAME AS Employee
# FROM Employee AS a JOIN Employee AS b
#      ON a.ManagerId = b.Id
#      AND a.Salary > b.Salary