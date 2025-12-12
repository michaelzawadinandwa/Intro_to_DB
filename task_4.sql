-- task_4.sql
-- Script to print full description of the books table without using DESCRIBE
-- Script to print full description of the books table using SHOW
SHOW COLUMNS FROM books;
ANALYZE TABLE books;

SELECT 
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = 'books';

SELECT
    COLUMN_NAME AS `Field`,
    COLUMN_TYPE AS `Type`,
    COLLATION_NAME AS `Collation`,
    IS_NULLABLE AS `Null`,
    COLUMN_KEY AS `Key`,
    COLUMN_DEFAULT AS `Default`,
    EXTRA AS `Extra`,
    PRIVILEGES AS `Privileges`,
    COLUMN_COMMENT AS `Comment`
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = 'books'
ORDER BY ORDINAL_POSITION;
