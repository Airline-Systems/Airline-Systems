import sys
import os

from suds import null, WebFault
from suds.client import Client
import logging


username = os.environ.get('FLIGHT_API_USERNAME')
apiKey = os.environ.get('FLIGHT_API_KEY')
url = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'


logging.basicConfig(level=logging.INFO)
api = Client(url, username=username, password=apiKey)
#print api


# Get the flights enroute
result = api.service.FlightInfo('QS1178', 1)
print(result)
#taf = api.service.NTaf('LKPR')
#print(taf)

#result = api.service.InboundFlightInfo('')
#print(result)



#print("Aircraft en route to KSMO:")
#for flight in flights:
    #print("%s (%s) \t%s (%s)" % ( flight['ident'], flight['aircrafttype'],
                                  #flight['originName'], flight['origin']))