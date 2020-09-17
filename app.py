import datetime, time
import base64
import streamlit as st
import pandas as pd

from views.home import render_home
from views.twitter import render_twitter
from views.instagram import render_instagram

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style.css")

render_home()

# Main text section
# pages = ["Home", "Twitter", "Instagram"]
# page = st.sidebar.selectbox("Select your page", pages)

# #HomeTWITTER Code
# if page == 'Twitter':
#   render_twitter()
# if page == 'Instagram':
#   render_instagram()
# elif page == 'Home':
#   render_home()
