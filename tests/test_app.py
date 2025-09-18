import unittest
from app.main import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)

    def test_add_product_get(self):
        response = self.app.get('/add_product')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add New Product', response.data)

    def test_categories_get(self):
        response = self.app.get('/categories')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Category List', response.data)

if __name__ == '__main__':
    unittest.main()
