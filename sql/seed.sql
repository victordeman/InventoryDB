-- Sample data for InventoryDB
INSERT INTO categories (category_name) VALUES
('Electronics'),
('Clothing');

INSERT INTO products (name, category_id, price, stock_quantity) VALUES
('Laptop', 1, 999.99, 50),
('T-Shirt', 2, 19.99, 200);
