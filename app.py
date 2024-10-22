import streamlit as st
import linearr_regression

# Sidebar Navigation
page = st.sidebar.selectbox("Choose a page", ["Linear Regression"])

# Navigate between pages
if page == "Linear Regression":
    linearr_regression.app()  # Load the Linear Regression page