# Write your MySQL query statement below


select t2.project_id , round(sum(t1.experience_years) / count(t2.employee_id), 2) as "average_years"
from Employee as t1 join Project as t2
on t1.employee_id = t2.employee_id
group by t2.project_id