# Write your MySQL query statement below




# select customer_number from orders
# group by customer_number
# having count(order_number)>1
# =max (select count(order_number) from orders group by customer_number)

select customer_number from orders
group by customer_number
order by count(order_number) DESC
limit 1