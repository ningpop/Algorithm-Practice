# Write your MySQL query statement below
select activity_date as day, count(distinct user_id) as active_users
from Activity a
group by activity_date
having activity_date between subdate(date('2019-07-27'), interval 29 day) and date('2019-07-27');