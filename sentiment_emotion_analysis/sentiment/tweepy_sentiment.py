from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy
import numpy as np
import pandas as pd

class Import_tweet_sentiment:

	consumer_key = "ZpuyQUWyiM09NQwLK9MTNfQHt"
	consumer_secret = "IQ6HWO4OsrxBNsXJILPw26fgzKHzuthKQvpuPo55xFXfdmYXpG"
	access_token = "2937336096-DrpKKvHQxG6ruCb78EtiStQF6XkL3KMtX6nLzX6"
	access_token_secret = "KKGedqXnm9VtuXFW4tMRMRKoiHUx8Ibd99yLlMZyIWhzX"

	def tweet_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		return df

	def get_tweets(self, handle):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = handle
		item = auth_api.user_timeline(id=account,count=10)
		df = self.tweet_to_data_frame(item)

		all_tweets = []
		for j in range(10):
			all_tweets.append(df.loc[j]['Tweets'])
		return all_tweets

		# Save extracted tweets from twitter here in the database

	def get_hashtag(self, hashtag):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = hashtag
		all_tweets = []

		for tweet in tweepy.Cursor(auth_api.search_tweets, q=account, lang='en').items(1):
			all_tweets.append(tweet.text)

		return all_tweets