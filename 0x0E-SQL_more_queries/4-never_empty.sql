-- This script creates the 'id_not_null' table with 'id'
-- and 'name' columns, where 'id' has a default value of 1.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT  1,
    name VARCHAR(256)
);
