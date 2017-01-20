#!/usr/bin/python3

# BT4Pi

# This bot interfaces with Twitter and the BT4U WebService API
# to automatically reply to direct messages with bus data.

import twitter
import time
from credentials import *

api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)

def getMessage():
    tweets = api.GetMentions()
    for thing in tweets:
        print (thing.user.screen_name)
    return
    
getMessage()
