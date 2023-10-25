# Write your MySQL query statement below


select t1.employee_id, t1.name, count(t2.employee_id) as reports_count, round(avg(t2.age), 0) as average_age
from Employees as t1 join Employees as t2
on t1.employee_id = t2.reports_to
group by t2.reports_to
order by t1.employee_id



# select t1.employee_id, t1.name, count(t2.reports_to) as reports_count, round(avg(t2.age), 0) as average_age
# from Employees as t1 join Employees as t2
# on t1.employee_id = t2.reports_to
# group by t2.reports_to
# order by t1.employee_id