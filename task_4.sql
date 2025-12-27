-- task_4.sql
-- Script to print full description of the books table
-- TABLE_NAME = 'Books'
-- TABLE_SCHEMA = 'alx_book_store'
SELECT
    COLUMN_NAME AS `Field`,
    COLUMN_TYPE AS `Type`,
    IS_NULLABLE AS `Null`,
    COLUMN_KEY AS `Key`,
    COLUMN_DEFAULT AS `Default`,
    EXTRA AS `Extra`
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = 'Books';