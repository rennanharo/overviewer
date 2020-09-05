import GetOldTweets3 as got
import pandas as pd

def get_tweets(search, location, language, startdate, enddate, maxtweet):
    """
      Uses GetOldTweets3 to gather twitter data

      Parameters:
        search(string): The query to perform
        location(string): Geographical location (name. E.g.: Paris, Brazil, Beijing) to perform the search
        language(string): Language which tweets were written in
        startdate(date DD/MM/YYYY): Gather tweets that have been published from this date
        enddata(date DD/MM/YYYY): Gather tweets that have been published up to this date
        maxtweet(int): Maximum number of tweets to gather

      Returns:
        tweets_df(pandas.dataframe): A pandas dataframe containing tweets that matched the parameters
    """

    # Apply the parameters to perform the query
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search)\
                                            .setSince(startdate)\
                                            .setUntil(enddate)\
                                            .setNear(location)\
                                            .setWithin("500mi")\
                                            .setMaxTweets(maxtweet)\
                                            .setLang(language)
    
    # Performs the query and return the result in a list
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    
    # Filter the result (tweet) to show only wanted information and assign them to text_tweets
    text_tweets = [[tw.text,
                tw.date,
                tw.retweets,
                tw.favorites,
                tw.mentions,
                tw.hashtags] for tw in tweet]
    
    # Transform text_tweets in a pandas dataframe
    tweets_df = pd.DataFrame(text_tweets, columns = ['Text', 'Date', 'Favorites', 'Retweets', 'Mentions', 'Hashtags'])
    
    return tweets_df