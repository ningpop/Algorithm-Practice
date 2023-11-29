# Write your MySQL query statement below

select t.request_at as Day, round(count(case when t.status <> 'completed' then 1 end) / count(*), 2) as `Cancellation Rate`
from Trips t
left join Users client_user
on t.client_id = client_user.users_id and client_user.role = 'client'
left join Users driver_user
on t.driver_id = driver_user.users_id and driver_user.role = 'driver'
where client_user.banned <> 'Yes' and driver_user.banned <> 'Yes' and t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at