# Write your MySQL query statement below


select UniqueProductId.product_id,
ifnull(LastChangedPrice.new_price, 10) as price
from
(
    select distinct product_id
    from Products) as UniqueProductId
    left join 
    (select Products.product_id, new_price
    from products 
     join (Select product_id, max(change_date) as change_date
           from products
          where change_date <= '2019-08-16'
          group by 
          product_id) as LastChangedDate Using (product_id, change_date)
    group by product_id) as LastChangedPrice using (product_id)
