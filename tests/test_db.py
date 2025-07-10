import unittest
from app.db import get_db_connection, fetch_products

class TestDatabase(unittest.TestCase):
    def test_connection(self):
        conn = get_db_connection()
        self.assertIsNotNone(conn)
        conn.close()

    def test_fetch_products(self):
        products = fetch_products()
        self.assertIsInstance(products, list)

if __name__ == '__main__':
    unittest.main()
