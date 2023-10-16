# Write your MySQL query statement below


# select t2.unique_id, t1.name 
# from Employees as T1 left join EmployeeUNI as T2
# on t1.id = t2.id;


# select T1.unique_id , T2.name
# from EmployeeUNI as T1 right join Employees as T2
# on T1.id = T2.id


select t1.unique_id, t2.name
from EmployeeUNI as t1 right join Employees as t2
on t1.id = t2.id