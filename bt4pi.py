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
        
    print(buslist[0:numBuses])
    outputStr = "The next {} buses for the {} route at stop {} are: ".format(len(buslist), routeName, stopCode)
    for i in range(len(buslist)):
        outputStr = outputStr + buslist[i] + " "
    print (outputStr) 
    return
    
getNextBus(3, 'HWDB', '1114')
