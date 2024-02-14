-- This script creates the database 'hbtn_0d_2' and the user 'user_0d_2'
-- with only the 'SELECT' privilege on the 'hbtn_0d_2' databse.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
