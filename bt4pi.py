#!/usr/bin/python3

# BT4Pi

# This bot interfaces with Twitter and the BT4U WebService API
# to automatically reply to direct messages with bus data.

import twitter
import time
from credentials import *

api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)
lastTweet = None

def getMessage():
    global lastTweet
    mostRecentTweet = api.GetMentions()[0]
    sn = mostRecentTweet.user.screen_name
    tweetID = mostRecentTweet.id_str
    txt = mostRecentTweet.text
    user, message = txt.split(" ", 1)
    
    if lastTweet != tweetID:   # If there is a new tweet available, then
        # parse message, check bus data, tweet to user
        newTweet = "@{} Test tweet 2!".format(sn)
        api.PostUpdate(newTweet)
    
    lastTweet = tweetID   # Updates lastTweet to most recent tweet
    
    print(sn, user, message, tweetID)
    
    return

while True:
    getMessage()
    time.sleep(15)   # Check every 15 seconds for a new tweet
