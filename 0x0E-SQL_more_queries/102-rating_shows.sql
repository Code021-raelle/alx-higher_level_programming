-- This script lists all shows from the 'hbtn_0d_tvshows_rate' database
-- by their total rating, sorted in descending order by the rating.

SELECT tv_shows.title, SUM(ratings.value) AS rating
FROM tv_shows
LEFT JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
