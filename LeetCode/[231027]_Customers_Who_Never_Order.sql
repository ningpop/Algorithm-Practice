select C.name Customers
from Customers C
left join Orders O
on C.id = O.customerId
where O.id is null;