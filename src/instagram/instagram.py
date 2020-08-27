import datetime, time
import base64
import os
import pandas as pd
import streamlit as st

from .cleaner import clean_json

def render_instagram():
  st.header('Instagram')
  tag = st.sidebar.text_input('Which hashtag do you want to scrape comments from?')
  maxp = st.sidebar.slider('How many posts do you want to scrape?', min_value=1, max_value=200)

  run_query = st.sidebar.button("Run the query")
  if run_query:
    with st.spinner("Wait..."):
      time.sleep(1)
    os.system(f'instagram-scraper --media-types none --tag {tag} --maximum {maxp} --comments --retry-forever --destination ./query_results')

    insta_df = clean_json(tag)
    st.dataframe(insta_df)

    st.success("Done!")
    st.balloons()

    csv = insta_df.to_csv(index=False, encoding='utf-8-sig')
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a style="font-size: 1.10rem; font-weight: 500; background-color: #0068c9; color: white; border-radius:0.5rem; padding:0.3rem 0.8rem;" href="data:file/csv base64,{b64}" encoding="utf-8-sig" download="tweets.csv">Download raw csv file</a>'
    st.markdown(href, unsafe_allow_html=True)
