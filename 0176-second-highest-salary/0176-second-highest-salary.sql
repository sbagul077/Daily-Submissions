-- # Write your MySQL query statement below
-- select 
--     ifnull((select distinct
--         salary
--     FROM
--         Employee
--     ORDER BY Salary desc
--     LIMIT 1 OFFSET 1), null)
--     as SecondHighestSalary;


select 
ifnull((select distinct 
        salary
    from Employee
    order by salary desc
    limit 1 offset 1), null)
    as SecondHighestSalary;