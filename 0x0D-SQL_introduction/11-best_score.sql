-- This script lists all records of the 'second_table' with a 'score' >= 10,
-- ordered by 'score' in descending order.

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
