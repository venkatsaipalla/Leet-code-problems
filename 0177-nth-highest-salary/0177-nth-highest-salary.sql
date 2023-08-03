CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N=N-1;
  RETURN (
      # Write your MySQL query statement below.
      
      select DISTINCT(salary) from Employee
      order by salary DESC limit 1 offset N
      
  );
END