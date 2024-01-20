# Write your MySQL query statement below
select class
from (
    select class, count(student) as cnt
    from Courses
    group by class
    having cnt >= 5
) as tb_cnt