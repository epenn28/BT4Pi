#!/user/bin/env python3

# BT4Pi

# This bot interfaces with Twitter and the BT4U WebService API
# to automatically reply to direct messages with bus data.

import requests
import xml.etree.ElementTree as ET

userData = {'routeShortName': 'HWDB', 'stopCode': '1114'}
r = requests.post("http://216.252.195.248/webservices/bt4u_webservice.asmx/GetNextDepartures", data=userData)
root = ET.fromstring(r.text)

for bus in root.findall('NextDepartures'):
    nextbus = bus.find('AdjustedDepartureTime').text
    print(nextbus)

