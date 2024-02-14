-- This script calculates the average temperature (Fahrenheit) by city,
-- ordered by temperature in descending order.

SELECT city, AVG(temperature) AS avg_temp
FROM weather_data
GROUP BY city
ORDER BY avg_temp DESC;\
