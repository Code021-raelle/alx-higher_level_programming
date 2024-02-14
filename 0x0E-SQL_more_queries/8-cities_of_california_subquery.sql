-- This script lists all the cities of California from the 'cities'
-- table, sorted in ascending ordre by 'cities.id'.

SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (SELECT states.id FROM states WHERE states.name = 'California')
ORDER BY cities.id ASC;
