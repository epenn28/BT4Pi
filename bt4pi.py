#!/usr/bin/python3

# BT4Pi

# This bot interfaces with Twitter and the BT4U WebService API
# to automatically reply to direct messages with bus data.

import twitter
import time
import requests
import xml.etree.ElementTree as ET
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
    
# Next bus function
def getNextBus(numBuses, routeName, stopCode):
    userData = {'routeShortName': routeName, 'stopCode': stopCode}
    r = requests.post("http://216.252.195.248/webservices/bt4u_webservice.asmx/GetNextDepartures", data=userData)
    root = ET.fromstring(r.text)
    buslist = []

    for nextbus in root.iter('AdjustedDepartureTime'):
        removeDate = nextbus.text.split(" ", 1)
        buslist.append(removeDate[1])
        
    if not buslist:
        outputStr = "Sorry, I didn't find any buses for that route at the time."
    else:
        outputStr = "The next {} buses for the {} route at stop {} are: ".format(numBuses, routeName, stopCode)
        for i in range(numBuses-1):
            outputStr = outputStr + buslist[i] + ", "
        outputStr = outputStr + buslist[numBuses] + "."
    print (outputStr) 

    return
    
def checkBus(routeName, stopCode):

    getRoutes = requests.post("http://216.252.195.248/webservices/bt4u_webservice.asmx/GetScheduledRoutes", data = {'stopCode': ''})
    getStops = requests.post("http://216.252.195.248/webservices/bt4u_webservice.asmx/GetScheduledStopCodes", data = {'routeShortName': routeName})
    
    routeRoot = ET.fromstring(getRoutes.text)
    stopRoot = ET.fromstring(getStops.text)
    
    routeList = []
    stopList = []
        
    for busRoute in routeRoot.iter('RouteShortName'):
        routeList.append(busRoute.text)
        
    for busStop in stopRoot.iter('StopCode'):
        stopList.append(busStop.text)
        
    if routeName in routeList:
        if stopCode in stopList:
            print("{} stop {} is valid".format(routeName, stopCode))
        else:
            print("Stop {} is not a valid stop for the {} route".format(stopCode, routeName))
    else:
        print("The {} route is not currently running!".format(routeName))
    
    return
    
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

#getNextBus(3, 'HWD', '1206')
#checkBus('HWDB', '1114')
#checkBus('HWD', '1206')
#checkBus('HWD', '1234')

#while True:
#    getMessage()
#    time.sleep(15)   # Check every 15 seconds for a new tweet
