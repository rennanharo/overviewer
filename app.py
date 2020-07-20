import streamlit as st

# Hiding the hamburguer menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title("Hello streamlit!")
st.subheader("Welcome to my first streamlit app1111!")