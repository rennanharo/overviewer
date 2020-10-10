import streamlit as st
import datetime

from models.app.img_display import img_to_bytes

def render_home():
  # Logo
  header_html = "<img src='data:image/png;base64,{}' class='home-logo'>".format(img_to_bytes("assets/files/Logo_Fiat_Chrysler_Automobiles.png"))
  st.markdown(header_html, unsafe_allow_html=True)

  # Main header
  st.markdown("<h1 class='main-header'>Explore o que o mundo está dizendo sobre nós.</h1>", unsafe_allow_html=True)
