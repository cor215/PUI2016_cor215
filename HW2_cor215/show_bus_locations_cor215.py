from __future__ import print_function
import json
import urllib2 
import os
import sys

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
key = str(sys.argv[1])
bus = str(sys.argv[2])
full_url = url + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus

response = urllib2.urlopen(full_url)
data = response.read().decode("utf-8")
dataMTA = json.loads(data)


location = dataMTA['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][3]['MonitoredVehicleJourney'
]['VehicleLocation']

numberOfActive = len(dataMTA['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])


print ("Bus Line : " + bus )
print ("Number of Active Buses : " + str(numberOfActive))

for i in range(numberOfActive):
    location = dataMTA['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i-1]['MonitoredVehicleJourney'
]['VehicleLocation']
    print("Bus " + str(i+1) + " is at latitude " + str(location['Latitude']) + " and longitude " + str(location['Longitude']) )
