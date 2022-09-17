import tweepy
import config   

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = 'covid -is:retweet'

response = client.search_recent_tweets(query=query, max_results=2)

print(response)