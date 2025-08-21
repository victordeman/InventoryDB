-- Common queries for InventoryDB
-- Get all products with category
SELECT p.product_id, p.name, c.category_name, p.price, p.stock_quantity
FROM products p
JOIN categories c ON p.category_id = c.category_id;

-- Update stock
UPDATE products
SET stock_quantity = stock_quantity - %s
WHERE product_id = %s;
