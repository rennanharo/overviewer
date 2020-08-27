import datetime, time
import base64
import streamlit as st
import pandas as pd

from src.pages.home import render_home
from src.twitter.get_tweets import get_tweets
from src.twitter.twitter import render_twitter
from src.instagram.instagram import render_instagram

# Page title and favicon
st.beta_set_page_config(page_title="Overviewer", 
                         page_icon="./assets/favicon.png",
                         initial_sidebar_state="expanded")

# Hiding the hamburguer menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Main text section
pages = ["Home","Twitter", "Instagram"]
page = st.sidebar.selectbox("Select your page", pages)


#HomeTWITTER Code
if page == 'Twitter':
  render_twitter()
if page == 'Instagram':
  render_instagram()
elif page == 'Home':
  render_home()
