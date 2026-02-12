# Write your MySQL query statement below

select emp.name as Employee
from Employee emp
right join employee mgr
 on emp.managerId = mgr.id
where emp.salary> mgr.salary