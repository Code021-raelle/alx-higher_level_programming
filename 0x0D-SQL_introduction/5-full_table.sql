-- This script prints the full description of the 'first_table' from the 'hbtn_0c_0' database.

SELECT CONCAT('CREATE TABLE `', TABLE_NAME, '` (', GROUP_CONCAT(CONCAT('\n  `', COLUMN_NAME, '` ', DATA_TYPE, IFNULL(CONCAT('(', CHARACTER_MAXIMUM_LENGTH, ')'), ''), ' ', IS_NULLABLE, ' ', EXTRA)), '\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci') AS Create_Table
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
