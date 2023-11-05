# Write your MySQL query statement below

select
  D.name as Department,
  E.name as Employee,
  E.salary as Salary
from Employee E
inner join (select departmentId, max(salary) as max_salary from Employee group by departmentId) as S
on E.departmentId=S.departmentId and E.salary=S.max_salary
inner join Department D
on E.departmentId=D.id