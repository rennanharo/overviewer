import streamlit as st

from models.app.img import img_to_bytes

def render_home():
  header_html = "<img src='data:image/png;base64,{}' class='home-logo'>".format(
    img_to_bytes("assets/files/Logo_Fiat_Chrysler_Automobiles.png")
  )
  st.markdown(header_html, unsafe_allow_html=True)
  
  st.markdown("<h1 style='text-align: center;'>Explore what the world is saying about us.</h1>", unsafe_allow_html=True)


  query = st.text_input('')
  search = st.button('Search')

  st.markdown('-'*7)
  st.markdown("""
                  You can check the [source code here.](https://github.com/rennanharo/overviewer)\n
                  Feel free to contribute with any suggestions or pull requests. Developed by [`Rennan Haro.`](https://github.com/rennanharo)
              """)