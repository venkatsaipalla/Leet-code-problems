# Write your MySQL query statement below

# with Temp as (

# select * from Employee
# )


# select distinct Employee.name as Employee from Employee 
# as a join Temp on Temp.id=Employee.managerId
# where Temp.salary<Employee.salary

SELECT
     a.NAME AS Employee
FROM Employee AS a JOIN Employee AS b
     ON a.ManagerId = b.Id
     AND a.Salary > b.Salary