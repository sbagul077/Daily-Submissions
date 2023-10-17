# Write your MySQL query statement below


# select t1.name , t2.bonus
# from Employee as t1 left join Bonus as t2
# on t1.empId = t2.empId
# where t2.bonus < 1000 or t2.bonus is NULL;



select emp.name, b.bonus
from employee as emp left join Bonus as b
on emp.empId = b.empId
where b.bonus < 1000 or b.bonus is NULL; 