import sys
import urllib2
import json

if __name__=='__main__':
    token=sys.argv[1]    
    bus=sys.argv[2]
    print "Bus Line : %s" % bus

    ## Code for local test    ##file=open("/Users/zhangyuxiang/Dropbox/Code/CUSP/PUI2015/week3/assignmet/vehicle-monitoring.json","rb")
    ##json_data=json.load(file)
    ##buses=json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    ##print "Number of Active Buses : %d" % len(buses)
    ##for i in range(len(buses)):
    ##    location=buses[i]['MonitoredVehicleJourney']["VehicleLocation"]
    ##    lat=location['Latitude']
    ##    lon=location['Longitude']
    ##    print "Bus %d is at latitude %f and longtitude %f" % (i, lat, lon)

    url="http://api.prod.obanyc.com/api/siri/vehicle-%%20monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (token, bus)
    request=urllib2.urlopen(url)
    json_data=json.load(request)
    buses=json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    print "Number of Active Buses : %d" % len(buses)
    for i in range(len(buses)):
        location=buses[i]['MonitoredVehicleJourney']["VehicleLocation"]
        lat=location['Latitude']
        lon=location['Longitude']
        print "Bus %d is at latitude %f and longtitude %f" % (i, lat, lon)
