-- This script lists all cities along with their corresponding state names
-- from the 'cities' and 'states' tables, sorted in ascending order by 'cities.id'.

SELECT cities.id, cities.name, (SELECT states.name FROM states WHERE states.id = cities.states_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
