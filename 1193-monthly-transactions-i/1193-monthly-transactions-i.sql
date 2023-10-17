# Write your MySQL query statement below

# DATE_FORMAT(trans_date, "%Y-%m") as month

select DATE_FORMAT(trans_date, "%Y-%m") as "month", 
country, 
count(id) as "trans_count", 
sum(if(state = "approved", 1, 0)) as "approved_count", 
sum(amount) as trans_total_amount,
sum(if(state = 'approved', amount,0)) as approved_total_amount
from Transactions
group by country, DATE_FORMAT(trans_date, "%Y-%m")

# sum(if(state = "approved", 1, 0)) as approved_count,
# sum(amount) as trans_total_amount,
# sum(if(state='approved',amount,0)) as approved_total_amount
# from Transactions

# {"headers": ["month", "country", "trans_count", "approved_count", "trans_total_amount", "approved_total_amount"], "values": [["2018-12", "US", 4, 3, 7000, 5000]]}


# {"headers": ["month", "country", "trans_count", "approved_count", "trans_total_amount", "approved_total_amount"], "values": [["2018-12", "US", 2, 1, 3000, 1000], ["2019-01", "US", 1, 1, 2000, 2000], ["2019-01", "DE", 1, 1, 2000, 2000]]}