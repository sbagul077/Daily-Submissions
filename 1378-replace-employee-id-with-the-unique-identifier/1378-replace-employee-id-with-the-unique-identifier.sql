# Write your MySQL query statement below


# Left join
select t2.unique_id, t1.name 
from Employees as T1 left join EmployeeUNI as T2
on t1.id = t2.id;


# Right Join
# select t1.unique_id, t2.name
# from EmployeeUNI as t1 right join Employees as t2
# on t1.id = t2.id