# Write your MySQL query statement below
select score,t.rank from (
select score , DENSE_RANK()
    over( order by score DESC ) as 'rank'
    from Scores
) as t