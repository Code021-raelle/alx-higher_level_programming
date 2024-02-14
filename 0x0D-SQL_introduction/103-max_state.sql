-- This script calculates the maximum temperature for each state,
-- ordered by state name.

SELECT state, MAX(temperature) AS max_temp
FROM weather_data
GROUP BY state
ORDER BY state;
