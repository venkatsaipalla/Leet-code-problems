# Write your MySQL query statement below




with temp as (
select * ,DATE_ADD(recordDate,interval -1   DAY) as yesterday,
    LAG(recordDate) over(order by recordDate) as previousDay,
    LAG(temperature) over(order by recordDate) as prviousTemp
    from Weather

)

select id from temp
where yesterday=previousDay
and prviousTemp<temperature