-- Check if customers already exist and insert only if they don't
INSERT INTO customer (customer_id, customer_name, email, address)
SELECT 2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'
WHERE NOT EXISTS (SELECT 1 FROM customer WHERE customer_id = 2);

INSERT INTO customer (customer_id, customer_name, email, address)
SELECT 3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'
WHERE NOT EXISTS (SELECT 1 FROM customer WHERE customer_id = 3);

INSERT INTO customer (customer_id, customer_name, email, address)
SELECT 4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.'
WHERE NOT EXISTS (SELECT 1 FROM customer WHERE customer_id = 4);