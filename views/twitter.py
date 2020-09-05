# Global imports
import datetime, time
import base64
import streamlit as st
import pandas as pd

# File specific imports
from models.twitter.get_tweets import get_tweets 
from models.twitter.wordcloud_twitter import word_cloud_twitter
from models.app.binary_downloader import get_binary_file_downloader_html
import models.app.SessionState as SessionState

## TODO --> Work on the SessionState variables to avoid reloading the page after changin any variables

def render_twitter():

  session_state = SessionState.get(run_query=False, gen_wordcloud=False, tweets="")

  st.markdown("""
                ### Twitter
                To work with **Twitter**, `customize your query in the sidebar to the left.`\n
                Then hit the `"Run the query"` button.
                If there are any tweets that match your criteria, a _preview_ (first 5 rows) of the datased
                will show up, followed by a link to download the _CSV_ file.
           """)
  st.markdown('-'*17)

  ## Search --> Text box
  ## TODO --> Add operators guide
  search = st.sidebar.text_input("What are you searching for?", "Fiat Toro")

  ## Location --> Text box (with map if possible)
  location = st.sidebar.text_input("Where are you searching it for?", "Brazil")

  ## Language --> Selector
  langs = ['any', 'ar', 'bg', 'bn', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'eu', 'fa', 'fi', 'fr', 'gu', 'he', 'hi', 'hr', 'hu', 'id', 'it', 'ja', 'kn', 'ko', 'mr', 'nl', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'sr', 'sv', 'ta', 'th', 'tr', 'uk', 'ur', 'vi', 'zh-cn', 'zh-tw']
  language = st.sidebar.selectbox("What language?", langs)

  ## Start date --> Date picker
  start_date = st.sidebar.date_input("Select the start date", datetime.date(2019, 7, 30))

  ## End date --> Date picker
  end_date = st.sidebar.date_input("Select the end date", datetime.date.today())

  ## Max tweets --> Slider
  max_tweets = st.sidebar.slider("What is the maximum number of Tweets you want? (The larger the number, the longer it takes to run.)", 100, 5000, 2500, 100)

  st.sidebar.text("")
  st.sidebar.text("")
  st.sidebar.markdown('-'*17)
  run_query = st.sidebar.button("Run the query")

  if run_query:
    session_state.run_query = True

  if session_state.run_query:
    with st.spinner("Wait..."):
      time.sleep(1)

    session_state.tweets = get_tweets(str(search), str(location), str(language), str(start_date), str(end_date), max_tweets)

    st.success("Done!")
    st.balloons()


    ## File preview
    st.markdown("### Preview the result")
    st.dataframe(session_state.tweets.head())
    rows = session_state.tweets['Date'].count()
    st.write(f'Number of tweets (rows): {rows}')

    ## Download file button
    csv = session_state.tweets.to_csv(index=False, encoding='utf-8-sig')

    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a style="font-size: 1.10rem; font-weight: 500; background-color: #0068c9; color: white; border-radius:0.5rem; padding:0.3rem 0.8rem;" href="data:file/csv;base64,{b64}" encoding="utf-8-sig" download="tweets.csv">Download raw csv file</a>'
    st.markdown(href, unsafe_allow_html=True)

  session_state.run_query = False

  input_stopwords = st.sidebar.text_area('Stopwords (comma separated)')
  gen_wordcloud = st.sidebar.button('Generate wordcloud')

  if gen_wordcloud:
    session_state.gen_wordcloud = True

  if session_state.gen_wordcloud:
    with st.spinner("Wait..."):
      time.sleep(1)
    word_cloud_twitter(input_stopwords, session_state.tweets)
    st.image("assets/outputs/word_clouds/twitter/tweets.png")

    st.markdown(get_binary_file_downloader_html('assets/outputs/word_clouds/twitter/tweets.png', 'WordCloud'), unsafe_allow_html=True)

  session_state.gen_wordcloud = False

  ## TODO
  # ## Dataset explorer view
  # st.markdown("-"*17)
  # st.markdown("""
  #   ## Dataset Filtering Section
  #   In this section you'll be able to easily filter your dataset to remove any unwanted data.
  # """)
  # column = st.selectbox("Which column do you want to edit?", list(tweets.columns))
  # term = list(st.text_input("What are the terms you want to filter out of your data?"))

  # for i in term:
  #   tweets_f = tweets[~tweets[column].str.contains(i)]

  # if st.button("Filter DF"):
  #   st.dataframe(tweets_f)