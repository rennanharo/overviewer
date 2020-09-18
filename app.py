import datetime, time
import base64
import streamlit as st
import pandas as pd

from views.visualizer import render_visualizer
from views.home import render_home
from models.app.params import get_params
import models.app.SessionState as SessionState

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style.css")

def main():
    render_home()

    session_state = SessionState.get(search=False, end_date='', start_date='', query_selector='', source_selector=[], limit='', ig_tag='', tt_query='', params={})
    
    if session_state.search == False:
        # Input section
        # The term to be searched for
        session_state.query_selector = st.text_input('O que você quer saber mais sobre?', 'Nova Strada')
        # The sources to search te term from
        session_state.source_selector = st.multiselect('Selecione as fontes', ['Instagram', 'Twitter'])

        # Display Instagram info
        if 'Instagram' in session_state.source_selector:
            st.info(f'O termo {session_state.query_selector} será pesquisado como uma hashtag (#) no Instagram.')
        
        # Display Twitter info and exclusive parameters
        if 'Twitter' in session_state.source_selector:
            # Start date
            session_state.start_date = st.date_input("Data de início", datetime.date(2019, 7, 30))
            # End date
            session_state.end_date = st.date_input("Data de término", datetime.date.today())
            st.info('Os campos de data só funcionam para filtrar informações do Twitter.')

        # Max number of posts to gather from each social media
        session_state.limit = st.slider("Qual o número máximo de posts que você quer buscar? (Quanto maior o número, mais tempo leva para rodar.)", 1, 500, 250, 10)

        session_state.ig_tag = session_state.query_selector.replace(' ', '').lower()
        session_state.tt_query = session_state.query_selector

    if session_state.source_selector != []:
        search = st.button('pesquisar')
        if search:
           session_state.search = True

    session_state.params = {
        'sources': session_state.source_selector,
        'limit': session_state.limit,
        'ig_tag': session_state.ig_tag,
        'tt_query': session_state.tt_query,
        'stdt': session_state.start_date,
        'endt': session_state.end_date,
    }
    
    
    if session_state.search:
        render_visualizer(session_state.params)
    session_state.search = False
    


    st.markdown('-'*7)
    st.markdown("""
                    You can check the [source code here.](https://github.com/rennanharo/overviewer)\n
                    Feel free to contribute with any suggestions or pull requests. Developed by [`Rennan Haro.`](https://github.com/rennanharo)
                """)

if __name__ == "__main__":
    main()