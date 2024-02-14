-- This script lists all records of the 'second_table' with a non-empty 'name' value, ordered by 'score' in descending order.

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
