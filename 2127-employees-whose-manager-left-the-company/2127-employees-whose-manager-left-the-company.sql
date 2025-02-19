/* Write your PL/SQL query statement below */


-- select employee_id from Employees
-- where salary < 30000 and manager_id not in (select employee_id from Employees)
-- order by employee_id;

select t1.employee_id
from Employees t1
left join Employees t2
on t1.manager_id = t2.employee_id
where t1.salary < 30000 and t2.employee_id is NULL and t1.manager_id IS NOT NULL
order by employee_id;