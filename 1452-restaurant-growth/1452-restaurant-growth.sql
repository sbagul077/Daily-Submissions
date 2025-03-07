/* Write your PL/SQL query statement below */
/* Write your PL/SQL query statement below */
WITH cte AS (
    SELECT visited_on, SUM(amount) AS total_amount
    FROM Customer
    GROUP BY visited_on
),
cte2 AS (
    SELECT 
        visited_on,
        SUM(total_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        ROUND(AVG(total_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
    FROM cte
)
SELECT 
    TO_CHAR(visited_on, 'YYYY-MM-DD') AS visited_on,
    amount,
    average_amount

FROM cte2
WHERE visited_on >= (SELECT MIN(visited_on) FROM cte2) + 6
ORDER BY visited_on;