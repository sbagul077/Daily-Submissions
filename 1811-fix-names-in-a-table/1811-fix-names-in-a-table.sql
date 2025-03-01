# Write your MySQL query statement below

select user_id, concat(UCASE(left(name, 1)), LCASE(SUBSTRING(name, 2))) as name from users
order by user_id;