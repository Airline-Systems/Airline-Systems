import random, yaml
from api.delay import DelayCoefficient
from api.flight import Metar_destination_api
from api.ticket_price_analysis import TicketPriceCoefficient
from helpers.daytime_factor import DaytimeProduct



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

def AveragePAXRatingInRoute(flight_number):
    flight_number = 2
    average_PAX_rating_in_route = random.uniform(2.9856, 3.3542)
    return average_PAX_rating_in_route

def AveragePAXRatingInRouteStatement(flight_number):
    flight_number = 1
    average_PAX_rating_in_route_statement = 'PAX are mostly satisfied'
    return average_PAX_rating_in_route_statement

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

def L1MeanPerformanceCoefficient(flight_number):
    flight_number = 1
    l1_mean_performance_coefficient = random.uniform(0.9856, 1.3542)
    return l1_mean_performance_coefficient

def R1MeanPerformanceCoefficient(flight_number):
    flight_number = 1
    r1_mean_performance_coefficient = random.uniform(0.9856, 1.3542)
    return r1_mean_performance_coefficient

def L2MeanPerformanceCoefficient(flight_number):
    flight_number = 1
    l2_mean_performance_coefficient = random.uniform(0.9856, 1.3542)
    return l2_mean_performance_coefficient

def CCSalesPerfomanceStatement(flight_number):
    flight_number = 1
    CC_sales_perfomance_statement = 'CCs are overperforming'
    return CC_sales_perfomance_statement

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

def AircraftRegistration(flight_number):
    flight_number = 1
    aircraft_registration = 'D-AISK'
    return aircraft_registration

def PreviousDestination(flight_number):
    flight_number = 1
    previous_destination = 'BER'
    return previous_destination

def DelayFromPreviousDestinationMin(flight_number):
    flight_number = 1
    delay_from_previous_destination_min = random.uniform(9,12)
    return delay_from_previous_destination_min

def FlightCoefficient(flight_number):
    flight_number = 1
    flight_coefficient = random.uniform(0.9856, 1.3542)
    return flight_coefficient

def DelayPredictionCoefficient(flight_number):
    flight_number = 1
    delay_prediction_coefficient = random.uniform(0.9856, 1.3542)
    return delay_prediction_coefficient

def DelayPredictionStatement(flight_number):
    flight_number = 1
    delay_prediction_statement = 'short delay is expected'
    return delay_prediction_statement

def PublicHolidayInOrigin(flight_number):
    flight_number = 1
    public_holiday_in_origin = 0
    return public_holiday_in_origin

def PublicHolidayInDestination(flight_number):
    flight_number = 1
    public_holiday_in_destination = 0
    return public_holiday_in_destination

def PublicHolidayInOriginCoefficient(flight_number):
    flight_number = 1
    public_holiday_in_origin_coefficient = 0
    return public_holiday_in_origin_coefficient

def PublicHolidayInDestinationCoefficient(flight_number):
    flight_number =1
    public_holiday_in_destination_coeffcicient = 0
    return public_holiday_in_destination_coeffcicient

def PublicHolidayStatement(flight_number):
    flight_number = 1
    public_holiday_statement = 0
    return public_holiday_statement

def Nationality1(flight_number):
    flight_number = 1
    nationality1='Russian Federation'
    return nationality1

def Nationality1Value(flight_number):
    flight_number = 1
    nationality_value = 78
    return nationality_value

def Nationality2(flight_number):
    flight_number = 1
    nationality2='United States of America'
    return nationality2

def Nationality1Value2(flight_number):
    flight_number = 1
    nationality_value2 = 24
    return nationality_value2

def Nationality3(flight_number):
    flight_number = 1
    nationality3='Germany'
    return nationality3

def Nationality1Value3(flight_number):
    flight_number = 1
    nationality_value3 = 22
    return nationality_value3

def Nationality4(flight_number):
    flight_number = 1
    nationality4 = 'Israel'
    return nationality4

def Nationality1Value4(flight_number):
    flight_number = 1
    nationality_value4 = 18
    return nationality_value4

def Nationality5(flight_number):
    flight_number = 1
    nationality5 = 'Italy'
    return nationality5

def Nationality1Value5(flight_number):
    flight_number = 1
    nationality_value5 = 17
    return nationality_value5

def PaxNationalityStatement(flight_number):
    flight_number = 1
    pax_nationality_statement = 'PAX are overspending'
    return pax_nationality_statement

def SportEventsInOrigin(flight_number):
    flight_number = 1
    sport_events_in_origin = 0
    return sport_events_in_origin

def CultureEventsInOrigin(flight_number):
    flight_number = 1
    culture_events_in_origin = 0
    return culture_events_in_origin

def SportEventsInDestination(flight_number):
    flight_number = 1
    sport_events_in_destination = 0
    return sport_events_in_destination

def CultureEventsInDestination(flight_number):
    flight_number = 1
    culture_events_in_destination = 0
    return culture_events_in_destination


def CuluturalEventsCoefficient(flight_number):
    flight_number = 1
    culutural_events_coefficient = 0
    return culutural_events_coefficient

def CuluturalEventsCoefficient(flight_number):
    flight_number = 1
    culutural_events_coefficient = 0
    return culutural_events_coefficient

def PublicEventsStatement(flight_number):
    flight_number = 1
    public_events_statement = "event"
    return public_events_statement

def DayTime(flight_number):
    flight_number = 1
    day_time = 0
    return day_time

def BreakfastCoefficient(flight_number):
    falight_number = 1
    breakfast_coefficient = random.uniform(0.5856, 0.8542)
    return breakfast_coefficient

def MainCourseCoefficient(flight_number):
    falight_number = 1
    main_course_coefficient = random.uniform(0.9856, 1.3542)
    return main_course_coefficient

def SnackCoefficient(flight_number):
    falight_number = 1
    snack_coefficient = random.uniform(0.7856, 0.9542)
    return snack_coefficient

def AlcoholCoefficient(flight_number):
    falight_number = 1
    alcohol_coefficient = random.uniform(1.1856, 1.3542)
    return alcohol_coefficient

def DayTimeStatement(flight_number):
    falight_number = 1
    day_time_statement = 'Evening flight'
    return day_time_statement

def FlightDurationMinutes(flight_number):
    flight_number = 1
    flight_duration_minutes = 95
    return flight_duration_minutes


def FlightDurationCoefficient(flight_number):
    flight_number = 1
    flight_duration_coefficient = random.uniform(0.9856, 1.1542)
    return flight_duration_coefficient

def FlightDurationStatement(flight_number):
    flight_number = 1
    flight_duration_statement = 'Short-haul flight'
    return flight_duration_statement

def FQTV(flight_number):
    flight_number = 1
    FQTV = random.uniform(8,12)
    return FQTV

def FQTVCoefficient(flight_number):
    flight_number = 1
    FQTV_coefficient = random.uniform(0.9856, 1.1542)
    return FQTV_coefficient

def FQTVStatement(flight_number):
    flight_number = 1
    FQTV_statement = 'More silver-card holders than usual'
    return FQTV_statement

def InboundTransit(flight_number):
    flight_number = 1
    inbound_transit = random.uniform(5,18)
    return inbound_transit

def OutboundTransit(flight_number):
    flight_number = 1
    outbound_transit = random.uniform(5,18)
    return outbound_transit

def TransitPAXCoefficient(flight_number):
    flight_number = 1
    transit_PAX_coefficient = random.uniform(0.9856, 1.1542)
    return transit_PAX_coefficient


