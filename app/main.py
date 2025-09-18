from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_db_connection, fetch_products, fetch_dashboard_stats, add_product, update_stock, fetch_categories, add_category

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # For flash messages

@app.route('/')
def index():
    stats = fetch_dashboard_stats()
    products = fetch_products()
    return render_template('index.html', stats=stats, products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product_route():
    if request.method == 'POST':
        name = request.form['name']
        category_id = request.form['category_id']
        price = request.form['price']
        stock_quantity = request.form['stock_quantity']
        try:
            add_product(name, int(category_id), float(price), int(stock_quantity))
            flash('Product added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error adding product: {str(e)}', 'error')
    categories = fetch_categories()
    return render_template('add_product.html', categories=categories)

@app.route('/update_stock', methods=['GET', 'POST'])
def update_stock_route():
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        try:
            update_stock(int(product_id), int(quantity))
            flash('Stock updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error updating stock: {str(e)}', 'error')
    return render_template('update_stock.html')

@app.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'POST':
        category_name = request.form['category_name']
        try:
            add_category(category_name)
            flash('Category added successfully!', 'success')
            return redirect(url_for('categories'))
        except Exception as e:
            flash(f'Error adding category: {str(e)}', 'error')
    categories = fetch_categories()
    return render_template('categories.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
