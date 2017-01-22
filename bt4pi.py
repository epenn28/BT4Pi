#!/user/bin/env python3

# BT4Pi

# This bot interfaces with Twitter and the BT4U WebService API
# to automatically reply to direct messages with bus data.

import requests
import xml.etree.ElementTree as ET

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
    
getNextBus(3, 'HWD', '1206')
checkBus('HWDB', '1114')
checkBus('HWD', '1206')
checkBus('HWD', '1234')
