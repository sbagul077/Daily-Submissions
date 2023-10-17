# Write your MySQL query statement below

select t1.customer_id , count(t1.customer_id) as "count_no_trans"
from Visits as t1 left join Transactions as t2
on t1.visit_id = t2.visit_id
where t2.transaction_id is NULL
group by t1.customer_id;


# select t1.customer_id, count(t1.customer_id) as "count_no_trans"
# from Visits as t1 left join Transactions as t2
# on t1.visit_id = t2.visit_id
# where t2.transaction_id is NULL
# group by t1.customer_id;
