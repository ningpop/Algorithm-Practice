# Write your MySQL query statement below

select Department, Employee, Salary
from (
  select
    D.name as Department,
    E.name as Employee,
    E.salary as Salary,
    dense_rank() over (partition by D.name order by E.salary desc) as Salary_rank
  from Employee as E
  inner join Department as D
  on E.departmentId = D.id
) as tb_salary_rank
where tb_salary_rank.Salary_rank < 4;