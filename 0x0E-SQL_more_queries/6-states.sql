-- This script creates the 'hbtn_0d_usa' database and the 'states'
-- table with 'id' and 'name' columns, where 'id' is unique,
-- auto-generated, cannot be null and is the primary key and 'anme' cannot be null.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
