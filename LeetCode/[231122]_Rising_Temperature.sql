# Write your MySQL query statement below

select id
from (
  select
    id,
    recordDate,
    temperature,
    IF(
      DATEDIFF(recordDate, LAG(recordDate) OVER (ORDER BY recordDate)) = 1,
      IFNULL(temperature - LAG(temperature) OVER (ORDER BY recordDate), 0),
      0
    ) as distance
  from Weather
) as tb_distance
where tb_distance.distance > 0;