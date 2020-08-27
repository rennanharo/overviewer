import os
import pandas
import streamlit as st

from .cleaner import clean_json

def render_instagram():
  st.header('Instagram')
  tag = st.sidebar.text_input('Which hashtag do you want to scrape comments from?')
  maxp = st.sidebar.slider('How many posts do you want to scrape?', min_value=1, max_value=200)

  run_query = st.sidebar.button("Run the query")
  if run_query:
    os.system(f'instagram-scraper --media-types none --tag {tag} --maximum {maxp} --comments --retry-forever --destination ./query_results')
    st.text('doneeeeeee!!!')

    insta_df = clean_json(tag)

    st.text('doneeeeeee running the cleaning part')
    st.dataframe(insta_df)

