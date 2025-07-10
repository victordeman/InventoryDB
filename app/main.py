# Streamlit app for InventoryDB
# app/main.py
import streamlit as st
import psycopg2
import yaml
import pandas as pd

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host=config["database"]["host"],
        port=config["database"]["port"],
        database=config["database"]["name"],
        user=config["database"]["user"],
        password=config["database"]["password"]
    )
    return conn

# Initialize Streamlit app
st.set_page_config(page_title="InventoryDB", page_icon="📦", layout="wide")
st.title("InventoryDB: Inventory Management System")
st.header("Manage Your Inventory with Ease")

# Sidebar for navigation
option = st.sidebar.selectbox("Choose Action", ["View Stock", "Add Product", "Sell Product", "Low Stock Alerts"])

# View Stock
if option == "View Stock":
    st.subheader("Current Inventory")
    conn = get_db_connection()
    df = pd.read_sql("SELECT id, name, category, quantity, price, reorder_level FROM products", conn)
    conn.close()
    st.dataframe(df)

# Add Product
elif option == "Add Product":
    st.subheader("Add New Product")
    with st.form("add_product_form"):
        name = st.text_input("Product Name")
        category = st.text_input("Category")
        quantity = st.number_input("Quantity", min_value=0, step=1)
        price = st.number_input("Price", min_value=0.0, format="%.2f")
        reorder_level = st.number_input("Reorder Level", min_value=0, step=1, value=10)
        submit = st.form_submit_button("Add Product")
        
        if submit:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO products (name, category, quantity, price, reorder_level) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                (name, category, quantity, price, reorder_level)
            )
            product_id = cur.fetchone()[0]
            cur.execute(
                "INSERT INTO transactions (product_id, transaction_type, quantity) VALUES (%s, %s, %s)",
                (product_id, "add", quantity)
            )
            conn.commit()
            cur.close()
            conn.close()
            st.success(f"Added {name} to inventory!")

# Sell Product
elif option == "Sell Product":
    st.subheader("Sell Product")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM products")
    products = cur.fetchall()
    product_dict = {name: id for id, name in products}
    cur.close()
    conn.close()
    
    with st.form("sell_product_form"):
        product_name = st.selectbox("Select Product", list(product_dict.keys()))
        quantity = st.number_input("Quantity to Sell", min_value=1, step=1)
        submit = st.form_submit_button("Sell Product")
        
        if submit:
            product_id = product_dict[product_name]
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT quantity FROM products WHERE id = %s", (product_id,))
            current_quantity = cur.fetchone()[0]
            if quantity <= current_quantity:
                cur.execute(
                    "INSERT INTO transactions (product_id, transaction_type, quantity) VALUES (%s, %s, %s)",
                    (product_id, "sell", quantity)
                )
                conn.commit()
                st.success(f"Sold {quantity} units of {product_name}!")
            else:
                st.error("Not enough stock available!")
            cur.close()
            conn.close()

# Low Stock Alerts
elif option == "Low Stock Alerts":
    st.subheader("Low Stock Alerts")
    conn = get_db_connection()
    df = pd.read_sql("SELECT name, quantity, reorder_level FROM products WHERE quantity <= reorder_level", conn)
    conn.close()
    if not df.empty:
        st.dataframe(df)
    else:
        st.info("No products below reorder level.")
