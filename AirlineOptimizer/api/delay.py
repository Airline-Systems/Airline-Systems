import yaml
from api.flight import *
from api.delay_factor import *


yaml_file = open('config_files/configurator.yaml')
configurator = yaml.load(yaml_file, Loader=yaml.FullLoader)

def DelayCoefficient():
    #array = api_call(amadeus, origin, destination, departureDate, departureTime, arrivalDate, arrivalTime, aicraftCode, carrierCode, flightNumber, duration)
    array = [0.41764125, 0.23375322, 0.15899977000000002, 0.18960576]
    no_delay_probability = array[0] * 100 #18.9%
    between_30_and_60_minutes = array[1] * 100 #
    between_60_and_120_minutes = array[2] * 100
    long_delay_probability = array[3] * 100 #41%

    #calculate a short delay probability
    short_delay_probability = between_30_and_60_minutes + between_60_and_120_minutes #38%

    #declare variables
    delay_from_previous_destination = 10
    arrival_coeficient = 1

    #logically calculate the delay coefficient
    if no_delay_probability > short_delay_probability and no_delay_probability > long_delay_probability:# or over_120_minutes_or_canceled:
        delay_coeficient = configurator['no_delay']
        delay_code = "no delay"

    elif short_delay_probability > no_delay_probability and short_delay_probability > long_delay_probability: # or less_than_30_minutes:
        delay_coeficient = configurator['short_delay']
        delay_code = "short delay"

    elif long_delay_probability > short_delay_probability and long_delay_probability > no_delay_probability: # or less_than_120_minutes:
        delay_coeficient = configurator['long_delay']
        delay_code = "long delay"
    else:
        delay_coeficient = "error"

    #logically calculate the arrival coefficient
    if delay_from_previous_destination < 20:
        arrival_coeficient = configurator['no_delay_on_arrival']
    elif delay_from_previous_destination < 60:
        arrival_coeficient = configurator['short_delay_on_arrival']

    elif delay_from_previous_destination > 60:
        arrival_coeficient = configurator['long_delay_on_arrival']

    #calculate the delay coefficient
    #delay_coeficient = delay_coeficient * arrival_coeficient
    delay_coefficient = 1.1
    return delay_coefficient
