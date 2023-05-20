import tweepy
import tkinter as tk

def tweet():
    text = text_entry.get()
    client.create_tweet(text=text)
    text_entry.delete(0, tk.END)

def retweet():
    tweet_id = tweet_id_entry.get()
    client.retweet(tweet_id)
    tweet_id_entry.delete(0, tk.END)

api_key = "jfZZi1So1y9KF4GOTIOfhbnG1"
api_secret = "PRl8E0EWwEtyg9mqvYrnOchC8BIrbPSsKCIqBChrl7PgoGuxcZ"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAHYsngEAAAAA5a8sALlgDEYm7qtcDi96Sn1R1%2Bw%3DRP4sDWkGSktWR9eqmzK5MfGLQEVsECC8EZVdbffdEcpLzkZPMG"
access_token = "1505689883414835203-96FBWoW3MFh7q7OWmWoFrk9Mpkq5qo"
access_token_secret = "CcXUush2eq6dQkzUsz0TYxwcXhI4mHwHPVY0Cyv8xQcmk"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Create the GUI
window = tk.Tk()
window.title("Twitter Bot")
window.geometry("500x300")
window.config(bg="#283747")

# Header
header_label = tk.Label(window, text="Twitter Bot", font=("Arial", 24), fg="#ffffff", bg="#283747")
header_label.pack(pady=20)

# Tweet Section
tweet_frame = tk.Frame(window, bg="#34495e")
tweet_frame.pack(pady=10)

tweet_label = tk.Label(tweet_frame, text="Tweet", font=("Arial", 18), fg="#ffffff", bg="#34495e")
tweet_label.pack(pady=10)

text_entry = tk.Entry(tweet_frame, font=("Arial", 12), width=40)
text_entry.pack(pady=5)

tweet_button = tk.Button(tweet_frame, text="Tweet", font=("Arial", 12), bg="#2ecc71", fg="#ffffff", padx=10, pady=5, command=tweet)
tweet_button.pack(pady=10)

# Retweet Section
retweet_frame = tk.Frame(window, bg="#34495e")
retweet_frame.pack(pady=10)

retweet_label = tk.Label(retweet_frame, text="Retweet", font=("Arial", 18), fg="#ffffff", bg="#34495e")
retweet_label.pack(pady=10)

tweet_id_entry = tk.Entry(retweet_frame, font=("Arial", 12), width=40)
tweet_id_entry.pack(pady=5)

retweet_button = tk.Button(retweet_frame, text="Retweet", font=("Arial", 12), bg="#2ecc71", fg="#ffffff", padx=10, pady=5, command=retweet)
retweet_button.pack(pady=10)

# Start the GUI
window.mainloop()
