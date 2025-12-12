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
    TABLE_SCHEMA = '$1'
    AND TABLE_NAME = 'books';
-- Check if customers already exist and insert only if they don't
INSERT INTO customer (customer_id, customer_name, email, address)