import psycopg2
from config import DB_CONFIG

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

def fetch_products():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.product_id, p.name, c.category_name, p.price, p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_id = c.category_id
    """)
    products = cur.fetchall()
    cur.close()
    conn.close()
    return products

def add_product(name, category_id, price, stock_quantity):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO products (name, category_id, price, stock_quantity) VALUES (%s, %s, %s, %s)",
        (name, category_id, price, stock_quantity)
    )
    conn.commit()
    cur.close()
    conn.close()

def update_stock(product_id, quantity):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE products SET stock_quantity = stock_quantity + %s WHERE product_id = %s",
        (quantity, product_id)
    )
    conn.commit()
    cur.close()
    conn.close()
