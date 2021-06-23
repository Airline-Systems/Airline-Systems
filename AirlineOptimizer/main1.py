import uvicorn, random
from fastapi import FastAPI, Depends
from datetime import datetime, timedelta
from api.delay import DelayCoefficient
from api.flight import Flight_api, FlightInfo
from helpers.booster import CountryCoefficient, TimeCoefficient, DurationCoefficient
from controller.controller import *
from api.culture_events import CultureEventDestination
from api.ticket_price_analysis import TicketPriceCoefficient, price_analysis
from helpers.daytime import *


app = FastAPI()

@app.get('/{flight_number}', tags=['Flight'])
async def airlineOptimizer(flight_number: int, occupancy=random.randint(160,189), occupancy2=random.randint(160,189)) -> dict:
    flight_number1 = flight_number
    flight_number2 = flight_number1 + 1
    flight_number1_temp = str('QS'+str(flight_number1))
    flight_number2_temp = str('QS'+str(flight_number2))

    flights = Flight_api(flight_number1_temp)
    flight_api = FlightInfo(flights)
    origin = flight_api[0]
    origin_city = flight_api[10]
    flight_number = flight_api[1]
    aircraft_type = flight_api[2]
    destination_icao = flight_api[3]
    departure_date = flight_api[5]
    departure_time = flight_api[6]
    arrival_date = flight_api[5]
    arrival_time = flight_api[9]
    carrier_code = flight_api[7]
    duration = flight_api[8]
    duration_statement = FlightDurationStatement(duration)
    destination = flight_api[4]
    destination_city = flight_api[11]
    daytime = DayTime(departure_time)

    male = random.randint(70,80)
    female = random.randint(70,80)
    children = occupancy - male - female
    inf = random.randint(0,4)

    nationality_majority_country = NationalityMajorityCountry(origin)
    nationality_majority_count =  NationalityMajorityCount(occupancy)
    nationality_minority_country = NationalityMinorityCountry(destination)
    nationality_minority_count =  NationalityMinorityCount(occupancy, nationality_majority_count)


    flights2 = Flight_api(flight_number2_temp)
    flight_api2 = FlightInfo(flights2)
    origin2 = flight_api2[0]
    origin_city2 = flight_api2[10]
    flight_number2 = flight_api2[1]
    aircraft_type2 = flight_api2[2]
    destination_icao2 = flight_api2[3]
    departure_date2 = flight_api2[5]
    departure_time2 = flight_api2[6]
    arrival_date2 = flight_api2[5]
    arrival_time2 = flight_api2[9]
    duration2 = flight_api2[8]
    destination2 = flight_api2[4]
    destination_city2 = flight_api2[11]
    daytime2 = DayTime(departure_time2)

    male2 = random.randint(70,80)
    female2 = random.randint(70,80)
    children2 = occupancy2 - male2 - female2
    inf2 = random.randint(0,4)

    nationality_majority_country2 = NationalityMajorityCountry(origin)
    nationality_majority_count2 =  NationalityMajorityCount(occupancy)
    nationality_minority_country2 = NationalityMinorityCountry(destination)
    nationality_minority_count2 =  NationalityMinorityCount(occupancy, nationality_majority_count)

    try:
        culture_event_destination = CultureEventDestination(destination)
        #culture_coefficients = float(culture_event_destination[0])
        culture_coefficients = 1
        culture_event_category_destination = culture_event_destination[1]
        culture_event_name_destination = culture_event_destination[2]
        culture_event_date_destination = culture_event_destination[3]
    except:
        culture_event_destination = 'no significant event'
        culture_coefficients = 1
        culture_event_category_destination = 'no significant event'
        culture_event_name_destination ='no significant event'
        culture_event_date_destination = departure_date2


    try:
        culture_event_origin = CultureEventDestination(origin)
        culture_event_category_origin = culture_event_origin[1]
        culture_event_name_origin = culture_event_origin[2]
        culture_event_date_origin = culture_event_origin[3]
    except:
        culture_event_origin = 'no significant event'
        culture_event_category_origin = 'no significant event'
        culture_event_name_origin = 'no significant event'
        culture_event_date_origin = departure_date

    panini = Product('panini', occupancy, culture_coefficients, daytime)
    chicken_bacon = Product('chicken_bacon', occupancy, culture_coefficients, daytime)
    cheese_baguette = Product('cheese_baguette', occupancy, culture_coefficients, daytime)
    quiche = Product('quiche', occupancy, culture_coefficients, daytime)

    tapas = Product('tapas', occupancy, culture_coefficients, daytime)
    penne = Product('penne', occupancy, culture_coefficients, daytime)
    lentil_salad = Product('lentil_salad', occupancy, culture_coefficients, daytime)
    noodle_soup = Product('noodle_soup', occupancy, culture_coefficients, daytime)
    couscous = Product('couscous', occupancy, culture_coefficients, daytime)

    macarons = Product('macaroons', occupancy, culture_coefficients, daytime)
    cheesecake = Product('cheesecake', occupancy, culture_coefficients, daytime)

    pilsner = Product('pilsner', occupancy, culture_coefficients, daytime)
    white_wine = Product('white_wine', occupancy, culture_coefficients, daytime)
    red_wine = Product('red_wine', occupancy, culture_coefficients, daytime)
    prosecco = Product('prosecco', occupancy, culture_coefficients, daytime)
    vodka = Product('vodka', occupancy, culture_coefficients, daytime)
    jameson = Product('jameson', occupancy, culture_coefficients, daytime)
    beefeater = Product('beefeater', occupancy, culture_coefficients, daytime)
    becherovka = Product('becherovka', occupancy, culture_coefficients, daytime)
    ripe_pear = Product('ripe_pear', occupancy, culture_coefficients, daytime)

    m_n_m = Product('m_n_m', occupancy, culture_coefficients, daytime)
    snickers = Product('snickers', occupancy, culture_coefficients, daytime)
    nutella = Product('nutella', occupancy, culture_coefficients, daytime)
    haribo = Product('haribo', occupancy, culture_coefficients, daytime)
    relax = Product('relax', occupancy, culture_coefficients, daytime)
    cricri =  Product('cricri', occupancy, culture_coefficients, daytime)
    pringles_original = Product('pringles_original', occupancy, culture_coefficients, daytime)
    pringles_sour = Product('pringles_sour', occupancy, culture_coefficients, daytime)
    olives = Product('olives', occupancy, culture_coefficients, daytime)
    peanuts = Product('peanuts', occupancy, culture_coefficients, daytime)

    schweppes = Product('schweppes', occupancy, culture_coefficients, daytime)
    fanta = Product('fanta', occupancy, culture_coefficients, daytime)
    coca_cola = Product('coca_cola', occupancy, culture_coefficients, daytime)
    coca_cola_zero = Product('coca_cola_zero', occupancy, culture_coefficients, daytime)
    sprite = Product('sprite', occupancy, culture_coefficients, daytime)
    birel = Product('birel', occupancy, culture_coefficients, daytime)

    cappy_apple = Product('cappy_apple', occupancy, culture_coefficients, daytime)
    cappy_orange =Product('cappy_orange', occupancy, culture_coefficients, daytime)
    rajec = Product('rajec', occupancy, culture_coefficients, daytime)


    ###################################Return flight###########################################

    panini2 = Product('panini', occupancy2, culture_coefficients, daytime2)
    chicken_bacon2 = Product('chicken_bacon', occupancy2, culture_coefficients, daytime2)
    cheese_baguette2 = Product('cheese_baguette', occupancy2, culture_coefficients, daytime2)
    quiche2 = Product('quiche', occupancy2, culture_coefficients, daytime2)

    tapas2 = Product('tapas', occupancy2, culture_coefficients, daytime2)
    penne2 = Product('penne', occupancy2, culture_coefficients, daytime2)
    lentil_salad2 = Product('lentil_salad', occupancy2, culture_coefficients, daytime2)
    noodle_soup2 = Product('noodle_soup', occupancy2, culture_coefficients, daytime2)
    couscous2 = Product('couscous', occupancy2, culture_coefficients, daytime2)

    macarons2 = Product('macaroons', occupancy2, culture_coefficients, daytime2)
    cheesecake2 = Product('cheesecake', occupancy2, culture_coefficients, daytime2)

    pilsner2 = Product('pilsner', occupancy2, culture_coefficients, daytime2)
    white_wine2 = Product('white_wine', occupancy2, culture_coefficients, daytime2)
    red_wine2 = Product('red_wine', occupancy2, culture_coefficients, daytime2)
    prosecco2 = Product('prosecco', occupancy2, culture_coefficients, daytime2)
    vodka2 = Product('vodka', occupancy2, culture_coefficients, daytime2)
    jameson2 = Product('jameson', occupancy2, culture_coefficients, daytime2)
    beefeater2 = Product('beefeater', occupancy2, culture_coefficients, daytime2)
    becherovka2 = Product('becherovka', occupancy2, culture_coefficients, daytime2)
    ripe_pear2 = Product('ripe_pear', occupancy2, culture_coefficients, daytime2)

    m_n_m2 = Product('m_n_m', occupancy2, culture_coefficients, daytime2)
    snickers2 = Product('snickers', occupancy2, culture_coefficients, daytime2)
    nutella2 = Product('nutella', occupancy2, culture_coefficients, daytime2)
    haribo2 = Product('haribo', occupancy2, culture_coefficients, daytime2)
    relax2 = Product('relax', occupancy2, culture_coefficients, daytime2)
    cricri2 =  Product('cricri', occupancy2, culture_coefficients, daytime2)
    pringles_original2 = Product('pringles_original', occupancy2, culture_coefficients, daytime2)
    pringles_sour2 = Product('pringles_sour', occupancy2, culture_coefficients, daytime2)
    olives2 = Product('olives', occupancy2, culture_coefficients, daytime2)
    peanuts2 = Product('peanuts', occupancy2, culture_coefficients, daytime2)

    schweppes2 = Product('schweppes', occupancy2, culture_coefficients, daytime2)
    fanta2 = Product('fanta', occupancy2, culture_coefficients, daytime2)
    coca_cola2 = Product('coca_cola', occupancy2, culture_coefficients, daytime2)
    coca_cola_zero2 = Product('coca_cola_zero', occupancy2, culture_coefficients, daytime2)
    sprite2 = Product('sprite', occupancy2, culture_coefficients, daytime2)
    birel2 = Product('birel', occupancy2, culture_coefficients, daytime2)

    cappy_apple2 = Product('cappy_apple', occupancy2, culture_coefficients, daytime2)
    cappy_orange2 =Product('cappy_orange', occupancy2, culture_coefficients, daytime2)
    rajec2 = Product('rajec', occupancy2, culture_coefficients, daytime2)

    salty_snacks = cricri + pringles_original + pringles_sour + peanuts + olives + tapas + lentil_salad + noodle_soup + couscous
    sweet_snacks = macarons + cheesecake + nutella + haribo + m_n_m + snickers
    sandwich = panini + chicken_bacon + cheese_baguette + quiche
    soft_drinks = schweppes + fanta + coca_cola + coca_cola_zero + sprite + birel + cappy_apple + cappy_orange + rajec
    alcohol_beverages = pilsner + white_wine + red_wine + prosecco
    shots = vodka + jameson + beefeater + becherovka + ripe_pear

    salty_snacks2 = cricri2 + pringles_original2 + pringles_sour2 + peanuts2 + olives2 + tapas2 + lentil_salad2 + noodle_soup2 + couscous2
    sweet_snacks2 = macarons2 + cheesecake2 + nutella2 + haribo2 + m_n_m2 + snickers2
    sandwich2 = panini2 + chicken_bacon2 + cheese_baguette2 + quiche2
    soft_drinks2 = schweppes2 + fanta2 + coca_cola2 + coca_cola_zero2 + sprite2 + birel2 + cappy_apple2 + cappy_orange2 + rajec2
    alcohol_beverages2 = pilsner2 + white_wine2 + red_wine2 + prosecco2
    shots2 = vodka2 + jameson2 + beefeater2 + becherovka2 + ripe_pear2








    flight = {'outbound_flight':{
                        'flight number': flight_number,
                        'departure date': departure_date,
                        'departure time': departure_time,
                        'arrival date': arrival_date,
                        'arrival time': arrival_time,
                        'origin': origin,
                        'origin city': origin_city,
                        'destination': destination,
                        'destination city': destination_city,
                        'aircraft': aircraft_type,
                        'PAX': occupancy,
                        'nationality majority': nationality_majority_country,
                        'nationality majority count': nationality_majority_count,
                        'nationality minority': nationality_minority_country,
                        'nationality minority count': nationality_minority_count,
                        'flight duration': duration,
                        'flight duration statement': duration_statement,
                        'daytime': daytime,
                        },

        'inbound_flight': {
            'flight number': flight_number2,
            'departure date': departure_date2,
            'departure time': departure_time2,
            'arrival date': arrival_date2,
            'arrival time': arrival_time2,
            'origin': origin2,
            'origin city': origin_city2,
            'destination': destination2,
            'destination city': destination_city2,
            'aircraft': aircraft_type2,
            'PAX': occupancy2,
            'nationality majority': nationality_majority_country2,
            'nationality majority count': nationality_majority_count2,
            'nationality minority': nationality_minority_country2,
            'nationality minority count': nationality_minority_count2,
            'flight_duration': duration2,
            'flight duration statement': duration_statement,
            'daytime2': daytime2,
        },

        'Catering_load': {
            'Sandwiches': {
                'Panini': panini + panini2,
                'Chicken&Bacon': chicken_bacon + chicken_bacon2,
                'Cheese Baguette': cheese_baguette + cheese_baguette2,
                'Quiche': quiche + quiche2,
            },
            'Salty snacks': {
                'Tapas Box': tapas + tapas2,
                'Penne Arrabbiata': penne + penne2,
                'Lentil Salad': lentil_salad + lentil_salad2,
                'Nissin Cup Noodles': noodle_soup + noodle_soup2,
                'Couscous Quinoa & Vegetables': couscous + couscous2,
            },
            'Sweat snacks': {
                'Macaroons 3pcs': macarons + macarons2,
                'Cheesecake': cheesecake + cheesecake2,
            },
            'Alcohol bevarages': {
                'Pilsner-Urquell': pilsner + pilsner2,
                'Savignon': white_wine + white_wine2,
                'Rulandske modre': red_wine + red_wine2,
                'Mionetto Prosecco': prosecco + prosecco2,
                'Absolut Vodka': vodka + vodka2,
                'Jameson': jameson + jameson2,
                'Beefeater Gin': beefeater + beefeater2,
                'Becherovka': becherovka + becherovka2,
                'Baron Hildprandt': ripe_pear + ripe_pear2,
            },
            'Snacks/Chocolates': {
                'M&Ms': m_n_m + m_n_m2,
                'Snickers': snickers + snickers2,
                'Nutella B-ready': nutella + nutella2,
                'Haribo Goldbears': haribo + haribo2,
                'Relax Puree': relax + relax2,
                'Cri Cri Gran Moravia': cricri + cricri2,
                'Pringles Original': pringles_original + pringles_original2,
                'Pringles Sour & Cream': pringles_sour + pringles_sour2,
                'Spanish Olives with garlic & Thyme': olives + olives2,
                'Salty Peanuts & Smoked Almonds': peanuts + peanuts2,
            },
            'Cold Bevarages': {
                'Schweppes': schweppes + schweppes2,
                'Fanta': fanta + fanta2,
                'Coca cola': coca_cola + coca_cola2,
                'Coca cola Zero': coca_cola_zero + coca_cola_zero2,
                'Sprite': sprite + sprite2,
                'Birel': birel + birel2,
            },
            'Water & Juices': {
                'Cappy Juice Apple': cappy_apple + cappy_apple2,
                'Cappy Juice Orange': cappy_orange + cappy_orange2,
                'Rajec': rajec + rajec2,
            },
        },
        'Category sales': {
            'products': {panini, birel, fanta},

        },

        'Factors': {
            'Airport_restaurants': {
                'Restaurant in orgin': CoefficientRestaurantsCategory1(flight_number),
                'Restaurants in destination': CoefficientRestaurantsCategory2(flight_number),
                'airport_restaurants_statement': AirportRestaurantsStatement(flight_number)
            },
            'Cabin crew': {
                'SC': sc_name(flight_number),
                'CC1': cc1_name(flight_number),
                'CC2': cc2_name(flight_number),
                'CC3': cc3_name(flight_number),
            },

            'Delay_prediction': {
                'no_delay_probability': NoDelayProbability(flight_number),
                'between_30_and_60_minutes': Between30And60Minutes(flight_number),
                'between_60_and_120_minutes': Between60And120Minutes(flight_number),
                'long_delay_probability': LongDelayProbability(flight_number),
            },
            'Public_events': {
                'Culture event rank destination': culture_coefficients,
                'Culture event date destination': culture_event_date_destination,
                'public_events_statement destination': culture_event_name_destination,
                'Culture event category destination': culture_event_category_destination,
                'Culture event date origin ': culture_event_date_origin,
                'Culture event name origin': culture_event_name_origin,
                'Culture event category origin': culture_event_category_origin

            },
            'sales_factor': SalesFactor(panini, panini2),
            'catering load general': [salty_snacks, sweet_snacks, sandwich, alcohol_beverages, soft_drinks, shots],
            'catering load general2': [salty_snacks2, sweet_snacks2, sandwich2, alcohol_beverages2, soft_drinks2, shots2],
            'pax distribution': [male, female, children, inf],
            'pax distribution2': [male2, female2, children2, inf2],
            'nationality count': [nationality_majority_count, nationality_minority_count],
            'nationality country': [nationality_majority_country, nationality_minority_country],
            'nationality count2': [nationality_majority_count2, nationality_minority_count2],
            'nationality country2': [nationality_majority_country2, nationality_minority_country2],

        },

    }

    return {"data": flight}

if __name__ == "__main__":
    uvicorn.run("main1:app", host="0.0.0.0", port=8000, reload=False)

#if __name__ == "__main__":
    #uvicorn.run("main1:app", port=8000, reload=True)


