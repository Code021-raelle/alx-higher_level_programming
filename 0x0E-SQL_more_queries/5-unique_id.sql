-- This script creates the 'unique_id' table with 'id'
-- and 'name' columns, where 'id' has a default value
-- of   1 and must be unique.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT   1 UNIQUE,
    name VARCHAR(256)
);
