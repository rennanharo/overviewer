import datetime, time
import base64
import os
import pandas as pd
import streamlit as st

# File specific imports
from models.instagram.cleaner import clean_json
from models.app.wordclouds import word_cloud_insta
from models.app.binary_downloader import get_binary_file_downloader_html
import models.app.SessionState as SessionState

## TODO --> Work on the SessionState variables to avoid reloading the page after changin any variables

def render_instagram():

  session_state = SessionState.get(run_query=False, gen_wordcloud=False, insta_df="")

  st.markdown("""
                ### Instagram
                To work with **Instagram**, `add the hashtag you want to scrape posts from in the sidebar to the left.`\n
                Then hit the `"Run the query"` button.
                If there are any posts that match your hashtag, a _preview_ (first 5 rows) of the datased will show up, followed by a link to download the _CSV_ file.
           """)
  st.markdown('-'*17)
  tag = st.sidebar.text_input('Which hashtag do you want to scrape comments from?')
  maxp = st.sidebar.slider('How many posts do you want to scrape?', min_value=1, max_value=500)

  run_query = st.sidebar.button("Run the query")

  if run_query:
    session_state.run_query = True
    
  if session_state.run_query:
    with st.spinner("Wait..."):
      time.sleep(1)
    os.chmod('assets/outputs/instagram/query_results',0o777)
    os.system(f"instagram-scraper --media-types none --tag {tag} --maximum {maxp} --comments --retry-forever --destination assets/outputs/instagram/query_results")

    session_state.insta_df = clean_json(tag)
    st.dataframe(session_state.insta_df)

    st.success("Done!")
    st.balloons()

    rows = session_state.insta_df['likes'].count()
    st.text(f'Amount of rows: {rows}')

    csv = session_state.insta_df.to_csv(index=False, encoding='utf-8-sig')
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a style="font-size: 1.10rem; font-weight: 500; background-color: #0068c9; color: white; border-radius:0.5rem; padding:0.3rem 0.8rem;" href="data:file/csv;base64,{b64}" encoding="utf-8-sig" download="{tag}.csv">Download raw csv file</a>'
    st.markdown(href, unsafe_allow_html=True)

  session_state.run_query = False
    
  input_stopwords = st.sidebar.text_area('Stopwords (comma separated)')
  gen_wordcloud = st.sidebar.button('Generate wordcloud')
  
  if gen_wordcloud:
    session_state.gen_wordcloud = True

  if session_state.gen_wordcloud:  
    with st.spinner("Wait..."):
      time.sleep(1)
    word_cloud_insta(input_stopwords, session_state.insta_df, tag)
    st.image(f"assets/outputs/word_clouds/instagram/{tag}.png")

    st.markdown(get_binary_file_downloader_html(f'assets/outputs/word_clouds/instagram/{tag}.png', 'WordCloud'), unsafe_allow_html=True)
  
  session_state.gen_wordcloud = False