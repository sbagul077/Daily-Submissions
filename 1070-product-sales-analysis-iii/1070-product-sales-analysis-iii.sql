# Write your MySQL query statement below


# select  t1.product_id, t1.year as first_year, t1.quantity, t1.price
# from Sales as t1
# where (t1.product_id, t1.year) IN (select product_id, min(year) from sales group by product_id)
# group by t1.product_id


select product_id, year as first_year, quantity, price
from sales
where (product_id, year) in (select product_id, min(year) from sales group by product_id)
