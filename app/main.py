import streamlit as st
from db import get_db_connection, fetch_products, add_product, update_stock

st.title("InventoryDB Management System")

# Display products
st.header("Product Inventory")
products = fetch_products()
st.dataframe(products)

# Add new product
st.header("Add New Product")
with st.form("add_product_form"):
    name = st.text_input("Product Name")
    category_id = st.number_input("Category ID", min_value=1, step=1)
    price = st.number_input("Price", min_value=0.01, format="%.2f")
    stock = st.number_input("Stock Quantity", min_value=0, step=1)
    submit = st.form_submit_button("Add Product")
    if submit:
        add_product(name, category_id, price, stock)
        st.success("Product added!")

# Update stock
st.header("Update Stock")
product_id = st.number_input("Product ID", min_value=1, step=1)
quantity = st.number_input("Quantity Change", step=1)
if st.button("Update Stock"):
    update_stock(product_id, quantity)
    st.success("Stock updated!")
