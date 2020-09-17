import datetime, time
import base64
import streamlit as st
import pandas as pd

from views.home import render_home
from views.twitter import render_twitter
from views.instagram import render_instagram

st.markdown(
    """
    <style>
    [class^="st-b"]  {
    }
    .st-cs {
    border-bottom-color: #0066cc
    }
    .st-cr {
        border-top-color: #0066cc
    }
    .st-cq {
        border-right-color: #0066cc
    }
    .st-cp {
        border-left-color: #0066cc
    }
    header .decoration {
        position: absolute;
        top: 0;
        right: 0;
        left: 0;
        height: 2px;
        background-image: -webkit-gradient(linear,left top,right top,from(#003366),to(#0066cc));
        background-image: -webkit-linear-gradient(left,#003366,#0066cc);
        background-image: linear-gradient(90deg,#003366,#0066cc);
        z-index: 120;
    }
    .btn-outline-info:not(:disabled):not(.disabled):focus, .btn-outline-info:not(:disabled):not(.disabled):hover, .btn-outline-primary:not(:disabled):not(.disabled):focus, .btn-outline-primary:not(:disabled):not(.disabled):hover, .btn-outline-secondary:not(:disabled):not(.disabled):focus, .btn-outline-secondary:not(:disabled):not(.disabled):hover {
        background-color: #fff;
        border-color: #0066cc;
        color: #0066cc;
    }
    .btn-outline-info:not(:disabled):not(.disabled):focus, .btn-outline-primary:not(:disabled):not(.disabled):focus, .btn-outline-secondary:not(:disabled):not(.disabled):focus {
        box-shadow: 0 0 0 0.2rem rgba(0,102,204,.5);
    }
    .st-fl {
        linear-gradient(to right, rgb(0,102,204) 0%, rgb(0,102,204) 63.2653%, rgb(230, 234, 241) 63.2653%, rgb(230, 234, 241) 100%)
    }
    .st-f7:hover {
        color: rgb(0,102,204);
    }
    .st-f6:hover {
        border-color: rgb(0,102,204);
    }
    .st-ef:focus {
        box-shadow: rgba(0,102,204, 0.5) 0px 0px 0px 0.2rem;
    }
    .st-f4:focus {
        color: rgb(0,102,204);
    }
    .st-f3:focus {
        border-color: rgb(0,102,204)
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Hiding the hamburguer menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Main text section
pages = ["Home", "Twitter", "Instagram"]
page = st.sidebar.selectbox("Select your page", pages)


#HomeTWITTER Code
if page == 'Twitter':
  render_twitter()
if page == 'Instagram':
  render_instagram()
elif page == 'Home':
  render_home()
