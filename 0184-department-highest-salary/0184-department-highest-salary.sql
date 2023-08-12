# Write your MySQL query statement below

select Department,Employee,Salary
from (
select d.name as Department,
e.name as Employee, e.salary as Salary,
RANK() over(partition by d.name order by e.salary DESC) as s_rank
from Employee as e  join Department as d on e.departmentId=d.id
)as t
where t.s_rank=1
    
# having 