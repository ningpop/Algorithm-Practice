# Write your MySQL query statement below
select distinct sp.name
from SalesPerson as sp
left join Orders as o
on sp.sales_id = o.sales_id
left join Company as c
on o.com_id = c.com_id
where sp.sales_id not in (
    select tb_o.sales_id
    from Orders as tb_o
    inner join Company as tb_c
    on tb_o.com_id = tb_c.com_id
    where tb_c.name = 'RED'
);