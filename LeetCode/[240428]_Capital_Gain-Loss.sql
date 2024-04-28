# Write your MySQL query statement below
select distinct s.stock_name, (ss.gain - bs.loss) as capital_gain_loss
from Stocks as s
inner join (
    select stock_name, sum(price) as loss
    from Stocks
    where operation = 'Buy'
    group by stock_name) as bs
on s.stock_name = bs.stock_name
inner join (
    select stock_name, sum(price) as gain
    from Stocks
    where operation = 'Sell'
    group by stock_name) as ss
on s.stock_name = ss.stock_name;