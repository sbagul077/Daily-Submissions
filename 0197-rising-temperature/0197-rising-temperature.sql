

# select t1.id as "Id"
# from weather as t1 join weather as t2
# on datediff(t1.recordDate, t2.recordDate) = 1
# and t1.temperature> t2.temperature;

select t1.id as "id"
from Weather as t1 join Weather as t2
on datediff(t1.recordDate , t2.recordDate) = 1
and t1.temperature > t2.temperature;