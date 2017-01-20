#!/usr/bin/python3

# BT4Pi

# This bot interfaces with Twitter and the BT4U WebService API
# to automatically reply to direct messages with bus data.

import twitter
import time
from credentials import *

api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)

def getMessage():
    mostRecentTweet = api.GetMentions()[0]
    sn = mostRecentTweet.user.screen_name
    txt = mostRecentTweet.text
    txt = txt.split(" ", 1)
    
    return txt[1]
    
message = getMessage()
print(message)
