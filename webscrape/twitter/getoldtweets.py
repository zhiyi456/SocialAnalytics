import snscrape.modules.twitter as sntwitter
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

sia = SentimentIntensityAnalyzer()


# Creating list to append tweet data to
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('singapore hackathon since:2017-07-05 until:2022-07-06').get_items()):
    if i>500:
        print("too many tweets")
        break
    sentiment = sia.polarity_scores(tweet.content)
    if sentiment['compound'] >= 0.05 :
        feeling = "Positive"
    elif sentiment['compound'] <= - 0.05 :
        feeling = "Negative"
    else :
        feeling = "Neutral"
    attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content, feeling])
    
# Creating a dataframe to load the list
tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet", "Feeling"])
tweets_df.to_csv('./webscrape/twitter/twitter_oldtweet.csv') 
