
# New York Times Developer API
import sys
import json
import csv
import requests

# variable Latitude and Longitude

if __name__ == '__main__':
	url = 'http://api.nytimes.com/svc/politics/v2/districts.json?lat=%s&lng=%s&api-key=732dbd5b2b8aea5fb63e433475f30265:18:73109944' % (sys.argv[1],sys.argv[2])
	request = requests.get(url)
	districtjsonfile = request.json()
	borough_info = districtjsonfile['results'][-1]['district']
	print borough_info

	# sys.argv[3] is a csvfile
	with open(sys.argv[3],'wb') as csvfile:
		filewriter = csv.writer(csvfile)

		row = [sys.argv[1],sys.argv[2],borough_info]
		filewriter.writerow(row)