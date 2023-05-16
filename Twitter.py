import tweepy

api_key = "jfZZi1So1y9KF4GOTIOfhbnG1"
api_secret = "PRl8E0EWwEtyg9mqvYrnOchC8BIrbPSsKCIqBChrl7PgoGuxcZ"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAHYsngEAAAAA5a8sALlgDEYm7qtcDi96Sn1R1%2Bw%3DRP4sDWkGSktWR9eqmzK5MfGLQEVsECC8EZVdbffdEcpLzkZPMG"
access_token = "1505689883414835203-96FBWoW3MFh7q7OWmWoFrk9Mpkq5qo"
access_token_secret = "CcXUush2eq6dQkzUsz0TYxwcXhI4mHwHPVY0Cyv8xQcmk"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

''' Text to tweet'''
#client.create_tweet(text ="Hello")
''' Tweet to like'''
#client.like("tweet_id")
''' Tweet to retweet''''
#client.retweet("tweet_id")
''' Tweet to reply '''
#client.create_tweet(in_reply_to_tweet_id="1658582166387785728", text ="text to retweet")

''' Seeing tweets on your timeline'''
#for tweet in api.home_timeline():
    #print(tweet.text)

''' Print tweets from another user's timeline'''

#person = client.get_user(username= "<username>").data.id

#for tweeet in clientt.get_users_tweets(person).data::
    #print(tweet.text)

''' Follow someone '''
#user_id = "<user_id_to_follow>"
#api.create_friendship(user_id)

''' Unfollow someone '''
#user_id = "<user_id_to_unfollow>"
#api.destroy_friendship(user_id)
