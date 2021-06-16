#!/usr/bin/python
import sys
from suds.client import Client
import os, sys
from suds.client import Client
import logging
import datetime
import json
import requests

from helpers.icao_to_iata_converter import airport


def Flight_api(flight_number):
    username = os.environ.get('FLIGHT_API_USERNAME')
    apiKey = os.environ.get('FLIGHT_API_KEY')
    fxmlUrl = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'

    logging.basicConfig(level=logging.INFO)
    api = Client(fxmlUrl, username=username, password=apiKey)

    # Get the flights enroute
    result = api.service.FlightInfo(flight_number, 1)
    flights = result['flights']
    return flights




def FlightInfo(flights):

    for flight in flights:
        origin = airport(flight['origin'])
        flightNumber = flight['ident']
        aircrafType = flight['aircrafttype']
        destination_icao = flight['destination']
        departureDate = datetime.datetime.fromtimestamp(flight['filed_departuretime']).strftime('%Y-%m-%d')
        departureTime = datetime.datetime.fromtimestamp(flight['filed_departuretime']).strftime('%H:%M')
        arrivalTime = datetime.datetime.fromtimestamp(flight['estimatedarrivaltime']).strftime('%H:%M')
        carrierCode = 'QS'
        duration = flight['filed_ete']
        destination = airport(destination_icao)
        flightInfo = [origin, flightNumber, aircrafType, destination_icao, destination, departureDate, departureTime, carrierCode, duration, arrivalTime]
        return flightInfo

def Metar_destination_api(destination_icao):
    username = os.environ.get('FLIGHT_API_USERNAME')
    apiKey = os.environ.get('FLIGHT_API_KEY')
    url = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'

    logging.basicConfig(level=logging.INFO)
    api = Client(url, username=username, password=apiKey)
    metar = api.service.Metar(destination_icao)
    return metar

#flights = Flight_api('LO528')
#flight_api = FlightInfo(flights)
#print(flight_api)









