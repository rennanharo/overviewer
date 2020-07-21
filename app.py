import streamlit as st
import GetOldTweets3 as got
import pandas as pd
import datetime, time

# Hiding the hamburguer menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.text("Pure text")
st.markdown("- [ ] Markdown ")

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
search = st.text_input("Where are you searching it for?", "Brazil")

## Start date --> Date picker
start_date = st.date_input("Select the start date", datetime.date(2019, 7, 30))

## End date --> Date picker
end_date = st.date_input("Select the end date", datetime.date(2019, 7, 30))

## Max tweets --> Slider
max_tweets = st.slider("What is the maximum number of Tweets you want?", 100, 5000, 2500, 100)

## Run query button
run_query = st.button("Run the query")
if run_query:
  ##TODO Call query function
  #tweets = get_tweets(str(search.value), str(location.value), str(s_date.value), str(e_date.value), max_tweets.value)
  pass

## Download file button
download_file = st.button("Download the CSV file")
if download_file:
  ##TODO Download file script
  pass

## Query status
##TODO Keep it async and finish running when query complete
with st.spinner("Wait..."):
  time.sleep(15)
st.success("Done!")

##TODO DF HEAD PREVIEW
st.dataframe(tweets.head())


#

#tweets.to_csv('tweets.csv', index = False)

# END TWITTER