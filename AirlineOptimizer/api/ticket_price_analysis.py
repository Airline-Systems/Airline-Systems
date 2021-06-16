import os, yaml
from amadeus import ResponseError, Client
import json
import requests

amadeus = Client(client_id=os.environ.get('AMADEUS_CLIENT_ID'), client_secret= os.environ.get('AMADEUS_CLIENT_SECRET_KEY'))

def price_analysis(origin, destination, departureDate):
    try:
        '''
        Returns price metrics of a given itinerary
        '''
        amadeus = Client(client_id=os.environ.get('AMADEUS_CLIENT_ID'),
                         client_secret=os.environ.get('AMADEUS_CLIENT_SECRET_KEY'))

        response = amadeus.analytics.itinerary_price_metrics.get(originIataCode= origin,
                                                                 destinationIataCode= destination,
                                                                 departureDate= departureDate)

        #corpus = response.data[ THE WHOLE JSON ][priceMetrics IS THE PART WHERE ALL THE VALUES ARE STORES], subsequently 0-min, 1-first quart, 3-median, 3-third quart, 4-max
        corpus = response.data[1]['priceMetrics']
        minimum = float(corpus[0]['amount'])
        first_quartile = float(corpus[1]['amount'])
        median = float(corpus[2]['amount'])
        third_quartile = float(corpus[3]['amount'])
        maximum = float(corpus[4]['amount'])

        price = {
            "minimum": minimum,
            "first_quartile": first_quartile,
            "median": median,
            "third_quartile": third_quartile,
            "maximum": maximum

        }
    except ResponseError as error:
        raise error
    return price

def TicketPriceCoefficient(origin, destination, departure_date):
    yaml_file = open('config_files/configurator.yaml')
    configurator = yaml.load(yaml_file, Loader=yaml.FullLoader)

    amadeus = Client(client_id=os.environ.get('AMADEUS_CLIENT_ID'), client_secret= os.environ.get('AMADEUS_CLIENT_SECRET_KEY'))
    avg_price = price_analysis(origin, destination, departure_date)


    flight_median_ticket_price = float(configurator['flight_median_ticket_price'])

    if flight_median_ticket_price < float(avg_price["minimum"]):
        ticket_coefficient = float(configurator['very_cheap'])
        tickets = "very cheap"
    elif flight_median_ticket_price >= float(avg_price["minimum"]) and flight_median_ticket_price < float(avg_price["first_quartile"]):
        ticket_coefficient = float(configurator['between_minimum_and_first_quartile'])
        tickets = "between minimum and first quartile"
    elif flight_median_ticket_price >= float(avg_price["first_quartile"]) and flight_median_ticket_price < float(avg_price["median"]):
        ticket_coefficient = float(configurator['under_medium_price'])
        tickets = "under medium price"
    elif flight_median_ticket_price >= float(avg_price["median"]) and flight_median_ticket_price < float(avg_price["third_quartile"]):
        ticket_coefficient = float(configurator['over_medium_price'])
        tickets = "over medium price"
    elif flight_median_ticket_price >= float(avg_price["third_quartile"]) and flight_median_ticket_price < float(avg_price["maximum"]):
        ticket_coefficient = float(configurator['just_under_maximum'])
        tickets = "just under maximum"
    elif flight_median_ticket_price > float(avg_price["maximum"]):
        ticket_coefficient = float(configurator['over_maximum'])
        tickets = "over maximum"
    else:
        ticket_coefficient = 0
        tickets = "error, not found"

    ticket_price_coefficient = [ticket_coefficient, tickets]
    print(ticket_price_coefficient)

    return ticket_price_coefficient



