# Write your MySQL query statement below


select 
    machine_id, 
    round(sum(case when activity_type='start' then timestamp*-1 else timestamp end)*1.0
    # ROUND(SUM(CASE WHEN activity_type='start' THEN timestamp*-1 ELSE timestamp END)*1.0
      / (select count(distinct process_id)), 3) as processing_time
from Activity
group by machine_id;

# SELECT 
#     machine_id,
#     ROUND(SUM(CASE WHEN activity_type='start' THEN timestamp*-1 ELSE timestamp END)*1.0
#     / (SELECT COUNT(DISTINCT process_id)),3) AS processing_time
# FROM 
#     Activity
# GROUP BY machine_id

# Select a.machine_id , ROUND(avg(b.timestamp - a.timestamp),3) as processing_time
# FROM Activity as a
# JOIN Activity as b
# ON a.machine_id = b.machine_id and a.process_id = b.process_id and a.activity_type = 'start' and b.activity_type = 'end'
# GROUP BY a.machine_id;