-- This script calculates the top 3 cities with the highest average
-- temperature during July and August,
-- ordered by temperature in descending order.

SELECT city, AVG(temperature) AS avg_temp
FROM weather_data
WHERE month IN ('July', 'August')
Group BY city
ORDER BY avg_temp DESC
LIMIT  3;
