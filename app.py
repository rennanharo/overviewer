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

st.title("Welcome to The Overviewer")
st.header("Analytics-friendly information extractor")
st.subheader("Let's start by customizing your query")
#st.text("Pure text")
#st.markdown("- [ ] Markdown ")

# TWITTER

def get_tweets(search, location, startdate, enddate, maxtweet):
    
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search)\
                                            .setSince(startdate)\
                                            .setUntil(enddate)\
                                            .setNear(location)\
                                            .setWithin("500mi")\
                                            .setMaxTweets(maxtweet)
    
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

## Search --> Text box
search = st.text_input("What are you searching for?", "Bolsonaro")

## Location --> Text box (with map if possible)
location = st.text_input("Where are you searching it for?", "Brazil")

## Start date --> Date picker
start_date = st.date_input("Select the start date", datetime.date(2019, 7, 30))

## End date --> Date picker
end_date = st.date_input("Select the end date", datetime.date.today())

## Max tweets --> Slider
max_tweets = st.slider("What is the maximum number of Tweets you want?", 100, 5000, 2500, 100)

## Run query button
run_query = st.button("Run the query")
if run_query:
  with st.spinner("Wait..."):
    time.sleep(1)

  tweets = get_tweets(str(search), str(location), str(start_date), str(end_date), max_tweets)
  
  st.dataframe(tweets.head())

  st.success("Done!")
  st.balloons()

  ## Download file button
  download_file = st.button("Download the CSV file")
  if download_file:
    ##TODO Download file script
    pass
  csv = tweets.to_csv(index=False)
  b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
  href = f'<a href="data:file/csv;base64,{b64}" download="tweets.csv">Download csv file</a>'
  st.markdown(href, unsafe_allow_html=True)

  ##TODO View DF online
  view_online = st.button("View the results online")



#tweets.to_csv('tweets.csv', index = False)

# END TWITTER