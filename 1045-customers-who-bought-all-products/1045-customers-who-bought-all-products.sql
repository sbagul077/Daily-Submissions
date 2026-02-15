# Write your MySQL query statement below
# Write your MySQL query statement below


-- select t1.customer_id, count(t1.customer_id) , count(t2.product_key)
-- from Customer as t1 
-- inner join Product t2
-- on t1.product_key = t2.product_key
-- group by t1.customer_id, t1.product_key
-- having count(t1.customer_id) = count(t2.product_key);


-- select customer_id from Customer group by customer_id having
-- count( distinct product_key) = (select count(product_key) from Product) ;

select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (Select count(product_key) from product);