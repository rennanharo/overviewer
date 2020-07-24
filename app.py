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


st.header("Welcome to The Overviewer")
st.markdown("""
                The Overviewer is an open source project to create a full-fledge tool to extract information from social media.

                Currently The Overviewer supports the following social media platforms:
                - Twitter

                You can check the [source code here.](https://github.com/rennanharo/overviewer)\n
                Feel free to contribute with any suggestions or pull requests. Let's build this together.\n
                `Developed by Rennan Haro 2020.`
           """)
st.markdown('-'*17)

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
                tw.hashtags,
                tw.geo] for tw in tweet]
    
    tweets_df = pd.DataFrame(text_tweets, columns = ['User', 'Text', 'Date', 'Favorites', 'Retweets', 'Mentions','Hashtags', 'Geolocation'])
    
    return tweets_df

  st.markdown('-'*17)
  st.markdown("""
                To work with Twitter, `customize your query in the sidebar to the right.`\n
                Then, hit the `"Run the query"` button.
           """)
  st.markdown('-'*17)


  ## Search --> Text box
  search = st.sidebar.text_input("What are you searching for?", "Fiat Toro")

  ## Location --> Text box (with map if possible)
  location = st.sidebar.text_input("Where are you searching it for?", "Brazil")

  ## Language --> Selector
  langs = ["BR", "EN"]
  language = st.sidebar.selectbox("What language?", langs)

  ## Start date --> Date picker
  start_date = st.sidebar.date_input("Select the start date", datetime.date(2019, 7, 30))

  ## End date --> Date picker
  end_date = st.sidebar.date_input("Select the end date", datetime.date.today())

  ## Max tweets --> Slider
  max_tweets = st.sidebar.slider("What is the maximum number of Tweets you want?", 100, 5000, 2500, 100)


  st.sidebar.text("")
  run_query = st.sidebar.button("Run the query")
  st.sidebar.markdown('-'*17)
  st.sidebar.text("Developed by Rennan Haro. 2020.")

  if run_query:
    with st.spinner("Wait..."):
      time.sleep(1)

    tweets = get_tweets(str(search), str(location), str(language), str(start_date), str(end_date), max_tweets)

    st.success("Done!")
    st.balloons()


    ## File preview
    st.subheader("Preview the query")
    st.dataframe(tweets.head())


    ## Download file button
    st.subheader("Download link sig")
    csv = tweets.to_csv(index=False, encoding='utf-8-sig')
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" encoding="utf-8-sig" download="tweets.csv">Download csv file</a>'
    st.markdown(href, unsafe_allow_html=True)


    ##View DF online
    ## Full dataframe
    st.subheader("Full file")
    st.dataframe(tweets)

  # END TWITTER