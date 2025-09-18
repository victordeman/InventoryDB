-- Common queries for InventoryDB
-- Get all products with category
SELECT p.product_id, p.name, c.category_name, p.price, p.stock_quantity
FROM products p
JOIN categories c ON p.category_id = c.category_id;

-- Update stock
UPDATE products
SET stock_quantity = stock_quantity + %s
WHERE product_id = %s;

-- Dashboard stats
SELECT COUNT(*) FROM products; -- Total products
SELECT COUNT(*) FROM categories; -- Total categories
SELECT COUNT(*) FROM products WHERE stock_quantity <= 10; -- Low stock
SELECT COUNT(*) FROM products WHERE stock_quantity = 0; -- Out of stock

-- Get all categories
SELECT category_id, category_name FROM categories;
