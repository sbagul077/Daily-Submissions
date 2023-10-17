# Write your MySQL query statement below


# select 
#     machine_id, 
#     round(sum(case when activity_type='start' then timestamp*-1 else timestamp end)*1.0
#     # ROUND(SUM(CASE WHEN activity_type='start' THEN timestamp*-1 ELSE timestamp END)*1.0
#       / (select count(distinct process_id)), 3) as processing_time
# from Activity
# group by machine_id;


select t1.machine_id,
round(avg(t2.timestamp - t1.timestamp), 3) as 'processing_time'
from Activity as t1
join Activity as t2
on t1.machine_id = t2.machine_id and t1.process_id = t2.process_id and t1.timestamp < t2.timestamp
group by t1.machine_id;