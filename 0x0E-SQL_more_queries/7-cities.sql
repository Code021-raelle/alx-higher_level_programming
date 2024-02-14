-- This script creates the 'hbtn_0d_usa' database and the 'cities'
-- table with 'id', 'state_id' and 'name' columns, where 'id' is
-- unique, auto-generated, cannot be null and is the primary key,
-- 'state_id' cannot be null and must reference the 'id' of the
-- 'states' table and 'name' cannot be null.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
