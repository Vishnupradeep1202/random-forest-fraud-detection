import streamlit as st

st.set_page_config(
    page_title="Credit Card Fraud ",
    page_icon="🤖",
    layout="wide")

pages = {
    "Main": [
        st.Page("pages/Home.py", title="Home", icon="🏠"),
        st.Page("pages/EDA.py", title="Data Analysis", icon="📊"),
        st.Page("pages/Model.py", title="Prediction", icon="🔮")]}

pg = st.navigation(pages)

pg.run()