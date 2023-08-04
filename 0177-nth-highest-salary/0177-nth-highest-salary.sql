CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
# SET N=N-1;
  RETURN (
      # Write your MySQL query statement below.
      
      # select DISTINCT(salary) from Employee
      # order by salary DESC limit 1 offset N
      
      select distinct salary from (
      select salary , DENSE_RANK() 
          OVER (order by salary DESC) as rankedSalary
          from Employee) as T
      where rankedSalary = N
      
  );
END

-- Why use dense_rank() instead of rank ?
/*
    DENSE_RANK() -- ranks are consecutive
    RANK() -- ranks are skipped
*/