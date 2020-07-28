import streamlit as st
import GetOldTweets3 as got
import pandas as pd
import datetime, time
import base64

# Hiding the hamburguer menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# End hiding the hamburguer menu


st.markdown("""
                ## Welcome to The Overviewer.
                The Overviewer is an open source project to create a full-fledge tool to extract information from social media.

                Currently The Overviewer supports the following social media platforms:
                - Twitter

                You can check the [source code here.](https://github.com/rennanharo/overviewer)\n
                Feel free to contribute with any suggestions or pull requests. Developed by [`Rennan Haro.`](https://github.com/rennanharo)
           """)
st.markdown('-'*7)

supported_tools = ["-","Twitter"]
st.markdown("### ~> Start by selecting your tool in the `selector below`. ")
tool = st.selectbox("Select your social media", supported_tools)


# TWITTER
if tool == "Twitter":

  def get_tweets(search, location, language, startdate, enddate, maxtweet):
    
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search)\
                                            .setSince(startdate)\
                                            .setUntil(enddate)\
                                            .setNear(location)\
                                            .setWithin("500mi")\
                                            .setMaxTweets(maxtweet)\
                                            .setLang(language)
    
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    
    text_tweets = [[tw.username,
                tw.text,
                tw.date,
                tw.retweets,
                tw.favorites,
                tw.mentions,
                tw.hashtags] for tw in tweet]
    
    tweets_df = pd.DataFrame(text_tweets, columns = ['User', 'Text', 'Date', 'Favorites', 'Retweets', 'Mentions', 'Hashtags'])
    
    return tweets_df

  st.markdown('-'*17)
  st.markdown("""
                ### Twitter
                To work with **Twitter**, `customize your query in the sidebar to the left.`\n
                Then hit the `"Run the query"` button.
                If there are any tweets that match your criteria, a _preview_ (first 5 rows) of the datased
                will show up, followed by a link to download the _CSV_ file.
           """)

  ## Search --> Text box
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
    with st.spinner("Wait..."):
      time.sleep(1)

    tweets = get_tweets(str(search), str(location), str(language), str(start_date), str(end_date), max_tweets)

    st.success("Done!")
    st.balloons()


    ## File preview
    st.markdown("### Preview the result")
    st.dataframe(tweets.head())
    rows = tweets['User'].count()
    st.write(f'Number of rows: {rows}')


    ## Download file button
    csv = tweets.to_csv(index=False, encoding='utf-8-sig')
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a style="font-size: 1.10rem; font-weight: 500; background-color: #0068c9; color: white; border-radius:0.5rem; padding:0.3rem 0.8rem;" href="data:file/csv;base64,{b64}" encoding="utf-8-sig" download="tweets.csv">Download csv file</a>'
    st.markdown(href, unsafe_allow_html=True)

  # END TWITTER