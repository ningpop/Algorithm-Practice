# Write your MySQL query statement below
select
    s.id as id,
    (case
        when LEAD(s.student) over (order by id) is null then s.student
        when MOD(tb_seat.num, 2) = 1 then LEAD(s.student) over (order by id)
        when MOD(tb_seat.num, 2) = 0 then LAG(s.student) over (order by id)
    end) as student
from Seat as s
inner join (select row_number() over(order by id) as num, id, student from Seat) as tb_seat
on s.id = tb_seat.id