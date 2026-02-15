# Write your MySQL query statement below

select
    t.id,
    CASE
        when t.p_id IS NULL THEN 'Root'
        when t.id NOT IN (SELECT DISTINCT p_id from Tree where p_id is not null) then 'Leaf'
        ELSE 'Inner'
    END as type
from Tree t;


-- SELECT 
--     t.id,
--     CASE
--         WHEN t.p_id IS NULL THEN 'Root'
--         WHEN t.id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
--         ELSE 'Inner'
--     END AS type
-- FROM Tree t;
