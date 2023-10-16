# Write your MySQL query statement below


select name from Customer
where referee_id is NULL OR referee_id <> 2;

# SELECT name FROM Customer
# WHERE referee_id !=2 OR referee_id IS NULL;