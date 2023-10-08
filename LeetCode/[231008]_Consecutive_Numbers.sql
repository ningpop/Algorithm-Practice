select distinct L1.num as ConsecutiveNums
from Logs as L1
inner join Logs as L2
on L1.id = L2.id+1
inner join Logs as L3
on L1.id = L3.id+2
where L1.num = L2.num and L1.num = L3.num;