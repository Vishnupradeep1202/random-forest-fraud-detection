import streamlit as st

st.title("Square Calculator")

number = st.number_input("Enter a number")

if st.button("Calculate"):
    square = number ** 2
    st.success(f"The square of {number} is {square}")
