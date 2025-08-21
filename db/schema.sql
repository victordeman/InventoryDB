-- db/schema.sql
CREATE DATABASE inventorydb;

\c inventorydb;

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    price DECIMAL(10, 2) NOT NULL,
    reorder_level INTEGER DEFAULT 10
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    transaction_type VARCHAR(20) CHECK (transaction_type IN ('add', 'sell')),
    quantity INTEGER NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a trigger to update product quantity
CREATE OR REPLACE FUNCTION update_quantity()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.transaction_type = 'add' THEN
        UPDATE products
        SET quantity = quantity + NEW.quantity
        WHERE id = NEW.product_id;
    ELSIF NEW.transaction_type = 'sell' THEN
        UPDATE products
        SET quantity = quantity - NEW.quantity
        WHERE id = NEW.product_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER quantity_trigger
AFTER INSERT ON transactions
FOR EACH ROW
EXECUTE FUNCTION update_quantity();
