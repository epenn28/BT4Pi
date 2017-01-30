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
        #newTweet = "@{} Test tweet 2!".format(sn)
        #api.PostUpdate(newTweet)
        print()
    
    lastTweet = tweetID   # Updates lastTweet to most recent tweet
    
    print(sn, user, message, tweetID)
    
    return
    
def parseMessage(text):
    collapsedText = " ".join(text.split())
    argsList = collapsedText.split(" ")
    numArgs = len(argsList)
    return argsList, numArgs
    
"""    if not argsList[0].isalpha():
        print("Invalid input- first word must be alphabetic')
    else:
        keyLower = argsList[0].lower()
        if numArgs == 1:
            if keyLower == "routes":
                print("Return currently running routes")
            else:
                print("Invalid input")
        elif numArgs == 2:
            if keyLower == "where":
                print("Check routeName to see if route is running")
            elif keyLower in routeNames:
                print("Check stopCode to display next 3 times for stop if route is running")
    
    elif numArgs == 2:          # if the message is two arguments
        if not argsList[0].isalpha():   # if the message doesn't start with a word
            print("Invalid input")
        else:                   # if the message does start with a word
            if argsList[0].lower() == "where":   # and the word is where
                print("Check routeName to see if route is running")
            elif in1.upper() in routeList
            
    elif numArgs == 3:
        route, stop, number, extra = text.split(" ", 3)
    else:
        print("Sorry, too many arguments")
        
    print("Route: {}\nStop: {}\nNumber: {}\nExtra: {}".format(route, stop, number, extra))
"""

argsList, numArgs = parseMessage("HWDB 1206")
print(argsList, numArgs)

#while True:
#    getMessage()
#    time.sleep(15)   # Check every 15 seconds for a new tweet
