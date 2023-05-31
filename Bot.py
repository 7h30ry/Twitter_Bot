import tweepy
import random
import time

api_key = "jfZZi1So1y9KF4GOTIOfhbnG1"
api_secret = "PRl8E0EWwEtyg9mqvYrnOchC8BIrbPSsKCIqBChrl7PgoGuxcZ"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAHYsngEAAAAA5a8sALlgDEYm7qtcDi96Sn1R1%2Bw%3DRP4sDWkGSktWR9eqmzK5MfGLQEVsECC8EZVdbffdEcpLzkZPMG"
access_token = "1505689883414835203-96FBWoW3MFh7q7OWmWoFrk9Mpkq5qo"
access_token_secret = "CcXUush2eq6dQkzUsz0TYxwcXhI4mHwHPVY0Cyv8xQcmk"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

tweet_ids = ["1615622233556406274", "1615740664695914499", "1616420531284107266"]

# Select a random tweet ID from the list
random_tweet_id = random.choice(tweet_ids)

word_list = ["Hello", "World", "Python", "Automation","Practice","Practical"]
random_word = random.choice(word_list)

# Tweet a word from the random list
tweet = client.create_tweet(text=random_word)
#tweet_id_reply = tweet[0].id

# Wait for 10-20 seconds
time.sleep(random.randint(10, 20))

# Comment on the tweeted word, replying to the random tweet ID
client.create_tweet(in_reply_to_tweet_id=random_tweet_id, text="Nice")
