# Write your MySQL query statement below


select name, COALESCE(sum(distance),0) travelled_distance 
from users t1
left join rides t2
on t1.id = t2.user_id
group by t1.id
order by travelled_distance desc, name asc