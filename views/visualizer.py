import streamlit as st

def render_visualizer(params):
  link = f"<a href='http://localhost:8501' target='_self'>Back</a>"
  st.markdown(link, unsafe_allow_html=True)
  
  st.write(params)