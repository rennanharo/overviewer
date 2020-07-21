import streamlit as st
import GetOldTweets3 as got
import pandas as pd

# Hiding the hamburguer menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title("Welcome to the Overviewer")
st.subheader("Subheader")


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

#tweets = get_tweets(search.value), str(location.value), str(s_date.value), str(e_date.value), max_tweets.value)

#tweets.to_csv('tweets.csv', index = False)

# END TWITTER