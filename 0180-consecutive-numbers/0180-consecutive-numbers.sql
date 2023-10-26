# Write your MySQL query statement below


select distinct l1.num as ConsecutiveNums
from logs as l1,
logs as l2,
logs as l3
where
l1.id = l2.id - 1
and l2.id = l3.id - 1
and l1.Num = l2.Num
and l2.Num = l3.Num