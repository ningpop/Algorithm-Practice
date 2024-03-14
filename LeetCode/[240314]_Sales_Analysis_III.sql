# Write your MySQL query statement below
select distinct p.product_id, p.product_name
from Product p
inner join Sales as s
on p.product_id = s.product_id
where p.product_id not in (select distinct product_id from Sales where sale_date < '2019-01-01' or '2019-03-31' < sale_date)