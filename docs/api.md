# API Documentation

## Flask Endpoints
- **GET /**: Display dashboard with product stats and recent products.
- **GET /add_product**: Render form to add a new product.
- **POST /add_product**: Add a new product to the database.
- **GET /update_stock**: Render form to update stock (optionally with \`product_id\` query param).
- **POST /update_stock**: Update stock for a product.
- **GET /categories**: Display category list and form to add a new category.
- **POST /categories**: Add a new category.

## Queries
- **List Products**: See \`sql/queries.sql\` for joining products and categories.
- **Dashboard Stats**: Queries for total products, categories, low stock, and out of stock.
- **Categories**: Fetch and add categories.
