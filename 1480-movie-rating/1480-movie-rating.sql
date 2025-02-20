# Write your MySQL query statement below

(select name as results
from MovieRating join users on MovieRating.user_id = users.user_id 
group by name
order by count(*) desc,name
LIMIT 1)

UNION ALL

(select title as results
from MovieRating join movies on MovieRating.movie_id = movies.movie_id 
where extract(year_month from created_at) = 202002
group by title
order by avg(rating) desc, title
LIMIT 1)