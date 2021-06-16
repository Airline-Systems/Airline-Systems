from amadeus import Client, ResponseError, Location
import os
import json
import pprint


amadeus = Client(client_id=os.environ.get('AMADEUS_CLIENT_ID'), client_secret= os.environ.get('AMADEUS_CLIENT_SECRET_KEY'))

def api_call(amadeus, origin, destination, departureDate, departureTime, arrivalDate, arrivalTime, aircraftCode, carrierCode, flightNumber, duration):
    try:
        '''
        How much delay can we expect on that flight?
        '''
        response = amadeus.travel.predictions.flight_delay.get(originLocationCode=origin, destinationLocationCode=destination,
                                                               departureDate=departureDate, departureTime=departureTime,
                                                               arrivalDate=arrivalDate, arrivalTime=arrivalTime,
                                                               aircraftCode=aircraftCode, carrierCode=carrierCode,
                                                               flightNumber=flightNumber, duration=duration)

        delay = [float(response.data[0]['probability']), float(response.data[1]['probability']), float(response.data[2]['probability']), float(response.data[3]['probability'])]

        return delay

    except ResponseError as error:
        raise error
