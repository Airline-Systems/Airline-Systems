import yaml
from helpers.iata_to_country_converter import IataToCountry
from api.flight import FlightInfo
from api.flight import *

yaml_file = open('config_files/configurator.yaml')
configurator = yaml.load(yaml_file, Loader=yaml.FullLoader)

def CountryCoefficient(destination):
    country = IataToCountry(destination)
    level_1 = ['Switzerland', 'Sweden', 'Norway', 'United States', 'Israel', 'Canada', 'Euro area', 'Australia', 'Denmark', 'New Zealand']
    level_2 = ['Britain', 'Germany', 'Singapore', 'Thailand', 'Czech Republic', 'South Korea', 'Chile', 'United Arab Emirates', 'Bahrain', 'Brazil', 'Costa Rica', 'Kuwait', 'Argentina', 'Colombia']
    level_3 = ['Japan', 'Saudi Arabia', 'Sri Lanka', 'Croatia', 'Honduras', 'Qatar', 'Nicaragua', 'Poland', 'China', 'Pakistan', 'Peru', 'Jordan', 'Guatemala']
    level_4 = ['Hungary','Philippines', 'Moldova', 'Vietnam', 'Oman', 'Egypt', 'Mexico', 'Hong Kong', 'India', 'Taiwan', 'Romania', 'Malaysia', 'Indonesia']
    level_5 = ['Azerbaijan', 'Ukraine', 'South Africa', 'Turkey', 'Russia', 'Lebanon']

    if country in level_1:
        country_coefficient = configurator['level_1_country']
    elif country in level_2:
        country_coefficient = configurator['level_2_country']
    elif country in level_3:
        country_coefficient = configurator['level_3_country']
    elif country in level_4:
        country_coefficient = configurator['level_4_country']
    elif country in level_5:
        country_coefficient = configurator['level_5_country']
    else:
        country_coefficient = "error"
    return country_coefficient

def TimeCoefficient(departure_time):
    departure_time = int(departure_time[:2])
    if departure_time < 10:
        day_part = "morning"
    elif departure_time >= 10 and departure_time < 14:
        day_part = "lunch"
    elif departure_time >= 14 and departure_time < 18:
        day_part = "afternoon"
    elif departure_time >= 18 and departure_time < 21:
        day_part = "dinner"
    elif departure_time >=21 and departure_time <24:
        day_part = "evening"
    else:
        day_part = "error"
    return day_part

def DurationCoefficient(departure_time, arrival_time):
    duration = int(arrival_time[:2]) - int(departure_time[:2])
    #duration = 2
    duration_coefficient = 1
    if duration > 2 and duration < 3:
        duration_coefficient = configurator['short_flight']
    elif duration >= 3 and duration <= 5:
        duration_coefficient = configurator['mid_flight']
    elif duration > 5:
        duration_coefficient = configurator['long_flight']
    return duration_coefficient










