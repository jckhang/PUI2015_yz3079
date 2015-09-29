import sys
import urllib2
import json
import csv

if __name__=='__main__':
    token=sys.argv[1]    
    bus=sys.argv[2]
    print "Bus Line : %s" % bus
    
    ## Code for local test
    ## file=open("/Users/zhangyuxiang/Dropbox/Code/CUSP/PUI2015/week3/assignmet/vehicle-monitoring.json","rb")
    ## json_data=json.load(file)
    ## buses=json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    ## print "Number of Active Buses : %d" % len(buses)
    ## with open('test.csv','wb') as csvfile:
    ##     writer=csv.writer(csvfile, delimiter=',')
    ##     writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status' ])
    ##     for i in range(len(buses)):
    ##         bus=buses[i]['MonitoredVehicleJourney']
    ##         lat=bus['VehicleLocation']['Latitude']
    ##         lon=bus['VehicleLocation']['Longitude']
    ##         if bus['OnwardCalls']=={}:
    ##             stop_name='NA'
    ##             stop_dist='NA'
    ##         else:
    ##             stop_name=bus['MonitoredCall']['StopPointName']
    ##             stop_dist=bus['OnwardCalls']['OnwardCall'][0]['Extensions']["Distances"]['PresentableDistance']
    ##         writer.writerow([lat, lon, stop_name, stop_dist])
 ## Code for api
    url="http://api.prod.obanyc.com/api/siri/vehicle-%%20monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (token, bus)
    request=urllib2.urlopen(url)
    json_data=json.load(request)
    buses=json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    print "Number of Active Buses : %d" % len(buses)
    with open(sys.argv[3],'wb') as csvfile:
        writer=csv.writer(csvfile, delimiter=',')
        writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status' ])
        for i in range(len(buses)):
            bus=buses[i]['MonitoredVehicleJourney']
            lat=bus['VehicleLocation']['Latitude']
            lon=bus['VehicleLocation']['Longitude']
            if bus['OnwardCalls']=={}:
                stop_name='NA'
                stop_dis='NA'
            else:
                stop_name=bus['MonitoredCall']['StopPointName']
                stop_dist=bus['OnwardCalls']['OnwardCall'][0]['Extensions']["Distances"]['PresentableDistance']
            writer.writerow([lat, lon, stop_name, stop_dist])
