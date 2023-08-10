# Write your MySQL query statement below

with temp as(
select * , LEAD(num,1) over() as next1,LEAD(num,2) over() as next2
from Logs
)

select distinct num as ConsecutiveNums from temp
where num=next1 and next1=next2;
