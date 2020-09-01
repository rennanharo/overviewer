import datetime, time
import base64
import os
import pandas as pd
import streamlit as st

from .cleaner import clean_json
from .wordcloud import word_cloud

def render_instagram():
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

  input_stopwords = st.sidebar.text_area('Stopwords (comma separated)')

  if run_query:
    with st.spinner("Wait..."):
      time.sleep(1)
    os.system(f'instagram-scraper --media-types none --tag {tag} --maximum {maxp} --comments --retry-forever --destination ./query_results')

    insta_df = clean_json(tag)
    st.dataframe(insta_df)

    st.success("Done!")
    st.balloons()

    rows = insta_df['likes'].count()
    st.text(f'Amount of rows: {rows}')

    csv = insta_df.to_csv(index=False, encoding='utf-8-sig')
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a style="font-size: 1.10rem; font-weight: 500; background-color: #0068c9; color: white; border-radius:0.5rem; padding:0.3rem 0.8rem;" href="data:file/csv;base64,{b64}" encoding="utf-8-sig" download="instagram_posts.csv">Download raw csv file</a>'
    st.markdown(href, unsafe_allow_html=True)
    
    #word_cloud_btn = st.sidebar.button('Generate word cloud')
    ##if word_cloud_btn:
    word_cloud(input_stopwords, insta_df, tag)
    st.image(f"word_clouds/instagram/{tag}.png")
