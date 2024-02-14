 -- This script converts the 'hbtn_0c_0' database,
 -- the 'first_table' table and the 'name' field
 -- in 'first_table' to UTF8 (utf8mb4, collate utf8mb4_unicode_ci).

 ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
 ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
 ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
 