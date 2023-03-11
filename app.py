import streamlit as st

st.title("Hello")

x = st.slider("Select a value")
st.write(x, "squared is", x * x)

streamlit run app.py
