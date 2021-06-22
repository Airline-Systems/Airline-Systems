import random, yaml
from api.delay import DelayCoefficient
from api.flight import Metar_destination_api
from api.ticket_price_analysis import TicketPriceCoefficient
from helpers.daytime_factor import DaytimeProduct
#from helpers.iata_to_country_converter import IataToCountry



yaml_file = open('config_files/configurator.yaml')
configurator = yaml.load(yaml_file, Loader=yaml.FullLoader)

yaml_file_config = open('config_files/optimal_load_coefficients.yaml')
configurator_load_coefficients = yaml.load(yaml_file_config, Loader=yaml.FullLoader)

yaml_file_weights = open('config_files/weights.yaml')
weights = yaml.load(yaml_file_weights, Loader=yaml.FullLoader)

delay_coefficients = 1


def Product(product, occupancy, culture_coefficients, daytime):
        mean_product_name = str('mean_sales_' + product)
        mean_sales = float(configurator_load_coefficients[mean_product_name])
        delay_coefficients = DelayCoefficient()
        daytime_coefficient = DaytimeProduct(product, daytime)
        optimal_load = int(mean_sales * occupancy * delay_coefficients * culture_coefficients * daytime_coefficient)
        if optimal_load < 1:
            optimal_load = 1
        else:
            optimal_load = optimal_load

        return optimal_load


#############################################################################################################################################################################
###################################################################           F A C T O R S                   #############################################################
#############################################################################################################################################################################







def TicketPriceCoefficient(origin, destination, departureDate):
    ticketPriceFactor = TicketPriceCoefficient(origin, destination, departureDate)
    print(ticketPriceFactor)
    return ticketPriceFactor

def TicketPriceOverMedia(flight_number):
    flight_number = 1
    ticketPriceOverMedian = 11.254
    print(ticketPriceOverMedian)
    return ticketPriceOverMedian

def TicketPriceConclusion(flight_number):
    ticketPriceConclusion = 'Average price is over median route price'
    return ticketPriceConclusion

def CoefficientRestaurantsCategory1(flight_number):
    flight_number = 1
    coefficient_restaurants_category_1 = random.uniform(0.9856, 1.3542)
    return coefficient_restaurants_category_1

def CoefficientRestaurantsCategory2(flight_number):
    flight_number = 1
    coefficient_restaurants_category_2 = random.uniform(0.9856, 1.3542)
    return coefficient_restaurants_category_2

def CoefficientRestaurantsCategory3(flight_number):
    flight_number = 1
    coefficient_restaurants_category_3 = random.uniform(0.9856, 1.3542)
    return coefficient_restaurants_category_3

def CoefficientRestaurantsCategory4(flight_number):
    flight_number = 1
    coefficient_restaurants_category_4 = random.uniform(0.9856, 1.3542)
    return coefficient_restaurants_category_4

def AirportRestaurantsStatement(flight_number):
    flight_number = 1
    airport_restaurants_statement = "all restaurants are open"
    return airport_restaurants_statement


def MeanSalesInRoute(flight_number):
    flight_number = 1
    mean_sales_in_route = random.uniform(98.56, 135.42)
    return mean_sales_in_route

def sc_name(flight_number):
    flight_number = 1
    sc_names = ['Jana Nebeska', 'Miluse Mila', 'Stepanka Krasna', 'Adela Nevecerelova']
    sc = sc_names[random.randrange(0,len(sc_names))]
    return sc

def cc1_name(flight_number):
    flight_number = 1
    cc1_names = ['Lubomir Mily', 'David Stastny', 'Michal Nejezchleba', 'Adam Cestny']
    cc1 = cc1_names[random.randrange(0,len(cc1_names))]
    return cc1

def cc2_name(flight_number):
    flight_number = 1
    cc2_names = ['Zorka Horka', 'Eliska Mlejnova', 'Tereza Jedina', 'Petr Cerny']
    cc2 = cc2_names[random.randrange(0,len(cc2_names))]
    return cc2

def cc3_name(flight_number):
    flight_number = 1
    cc3_names = ['Premysl Otakar', 'Alexandr Veliky', 'Ivan Hrozny', 'Anezka Ceska']
    cc3 = cc3_names[random.randrange(0,len(cc3_names))]
    return cc3

def NoDelayProbability(flight_number):
    flight_number = 1
    no_delay_probability = 0.23375322
    return no_delay_probability

def Between30And60Minutes(flight_number):
    flight_number = 1
    between_30_and_60_minutes = 0.41764125
    return between_30_and_60_minutes

def Between60And120Minutes(flight_number):
    flight_number = 1
    between_30_and_60_minutes = 0.41764125
    return between_30_and_60_minutes

def LongDelayProbability(flight_number):
    flight_number = 1
    long_delay_probability = 0.018960576
    return long_delay_probability

def MetarOrigin(flight_number):
    flight_number = 1
    metar_origin = Metar_destination_api('LKPR')
    return metar_origin

def MetarDestination(destination_icao):
    metar_destination = Metar_destination_api(destination_icao)
    return metar_destination

def DelayFromPreviousDestinationMin(flight_number):
    flight_number = 1
    delay_from_previous_destination_min = random.uniform(9,12)
    return delay_from_previous_destination_min

def FlightCoefficient(flight_number):
    flight_number = 1
    flight_coefficient = random.uniform(0.9856, 1.3542)
    return flight_coefficient

def DayTime(flight_number):
    flight_number = 1
    day_time = 0
    return day_time


def FlightDurationCoefficient(flight_number):
    flight_number = 1
    flight_duration_coefficient = random.uniform(0.9856, 1.1542)
    return flight_duration_coefficient

def FlightDurationStatement(duration):
    duration_hours = int(duration[1])
    if duration_hours < 1:
        flight_duration_statement = 'very short flight'
    elif duration_hours >= 1 and duration_hours < 2:
        flight_duration_statement = 'short flight'
    elif duration_hours >= 2 and duration_hours < 3:
        flight_duration_statement = 'midrange flight'
    elif duration_hours >= 3 and duration_hours < 4:
        flight_duration_statement = 'long flight'
    if duration_hours >= 4:
        flight_duration_statement = 'very long flight'
    return flight_duration_statement



def SalesFactor(panini, panini2):
    panini = (panini + panini2)/2
    if panini < 2:
        prediction_factor = 'Very low sales'
    elif panini >= 4 and panini <= 8:
        prediction_factor = 'Low sales'
    elif panini >= 8 and panini <= 12:
        prediction_factor = 'Average sales'
    elif panini >= 12 and panini <= 16:
        prediction_factor = 'Overaverage sales'
    elif panini >= 16 and panini <= 20:
        prediction_factor = 'High sales'
    elif panini > 20:
        prediction_factor = 'Very high sales'

    return prediction_factor

def NationalityMajorityCountry(origin):
    #country = IataToCountry(origin)
    country = "Czech republic"
    return country

def NationalityMajorityCount(occupancy):
    nationality_count = occupancy/2 + random.randint(5,25)
    return nationality_count

def NationalityMinorityCountry(destination):
    #country = IataToCountry(destination)
    country = "Spain"
    return country

def NationalityMinorityCount(occupancy, national_majority_count):
    nationality_count = occupancy - national_majority_count + random.randint(5,25)
    return nationality_count






