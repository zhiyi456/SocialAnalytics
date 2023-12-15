#scrape tweets from twitter
import tweepy
from tweepy import OAuthHandler
import pandas as pd
# from nltk.sentiment import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Consumer/Access key/secret/token obtained from Twitter
# You should have created a Twitter app and gotten these keys.
# Do NOT share your key/secret/token with other students.
# Below the keys & tokens are mine. Replace them with your own! (otherwise Twitter will quickly halt my service)

#is434test
consumer_key    = 'FWDYm0zJc8qvEXOLAvMjyJIQ5'
consumer_secret = 'iLzLWLlA6nVW4aE8FD68aDpITZ2XeaUb9yS6zsA7AEPma9of3q'
access_token    = '1313832251830923266-XOrPHrark9MMPN7TuDQiQpVPraAdMe'
access_secret   = 'hf5zc16eYnwXt7a8PNerGlxtyWnk2MOfDLRXs5zsOz1oe'

#is434R
#consumer_key    = 'vWADtcRNrAEgCRhKcsR969Big'
#consumer_secret = 'DvPjTUSVbV5E2S5mtj3VwnKRkxJicuq9kH5Q1HNYQPrcaoeioC'
#access_token    = '1561964990596550656-PEFsdlQ9gFvUf2mt9cFDE4Ga7HXNiG'
#access_secret   = 'rf0uRFOchl3Wv2JsPoMfC6im8ij989ARzs1NlTzqnGHwo'

# The following two lines create an authorization object with your above authentication info.
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# This line finally calls Twitter's Rest API.
api = tweepy.API(auth)

print("hello")
sia = SentimentIntensityAnalyzer()
output = []
# This FOR loop will retrieve the latest 100 tweets - based on search term(s)
for tweet in tweepy.Cursor(api.search_tweets, q="singapore hackathon", lang="en", count="100", max_id="1575349787225997312").items(100):
    # print out user's screen name & tweet text
    print("----------------------------------------------------")
    print ('ID: ' + str(tweet.id) + ' Tweet by: @' + tweet.user.screen_name + ' Created at ' + str(tweet.created_at))
    print('       ' + tweet.text)
    sentiment = sia.polarity_scores(tweet.text)
    if sentiment['compound'] >= 0.05 :
        feeling = "Positive"
    elif sentiment['compound'] <= - 0.05 :
        feeling = "Negative"
    else :
        feeling = "Neutral"
    output.append({"tweetId" : tweet.id, "username" : tweet.user.screen_name, "date" : tweet.created_at, "text" : tweet.text, "feeling" : feeling})
    

# Use search function with care. As free user, you have limitation on how much requests can be made per time unit.
# See reference here: https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits
# Otherwise, you will easily get Twitter error response: 'status code = 429'
# Returns tweets created before the given date indicated by parameter 'until'. Date should be formatted as YYYY-MM-DD.
# Keep in mind that the search index has a 7-day limit. In other words, no tweets will be found for a date older than one week.


df = pd.DataFrame(output)
df.to_csv('output.csv')
