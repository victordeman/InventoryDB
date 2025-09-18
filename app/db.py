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

def fetch_dashboard_stats():
    conn = get_db_connection()
    cur = conn.cursor()
    stats = {}
    cur.execute("SELECT COUNT(*) FROM products")
    stats['total_products'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM categories")
    stats['total_categories'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM products WHERE stock_quantity <= 10")
    stats['low_stock'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM products WHERE stock_quantity = 0")
    stats['out_of_stock'] = cur.fetchone()[0]
    cur.close()
    conn.close()
    return stats

def add_product(name, category_id, price, stock_quantity):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO products (name, category_id, price, stock_quantity) VALUES (%s, %s, %s, %s)",
            (name, category_id, price, stock_quantity)
        )
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def update_stock(product_id, quantity):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE products SET stock_quantity = stock_quantity + %s WHERE product_id = %s",
            (quantity, product_id)
        )
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def fetch_categories():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT category_id, category_name FROM categories")
    categories = cur.fetchall()
    cur.close()
    conn.close()
    return categories

def add_category(category_name):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO categories (category_name) VALUES (%s)",
            (category_name,)
        )
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()
