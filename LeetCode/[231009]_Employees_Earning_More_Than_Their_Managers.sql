select E1.name as Employee
from Employee as E1
inner join Employee as E2
on E1.managerId = E2.id
where E1.salary > E2.salary;