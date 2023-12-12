# Write your MySQL query statement below

select customer_number
from (
    select customer_number, count(*) as order_count from Orders group by customer_number order by order_count desc
) as tb_Order_count
limit 1;