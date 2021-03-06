import yaml

def DaytimeProduct(product, daytime):
    #yaml_file = open('config_files/configurator.yaml')
    # configurator = yaml.load(yaml_file, Loader=yaml.FullLoader)

    morning = ['americano', 'cappucino', 'tea', 'cheesecake', 'macaroons']
    late_morning = ['americano', 'cappucino', 'tea', 'cheesecake', 'macaroons', 'm&m', 'snickers', 'nutella', 'relax']
    lunch = ['panini', 'chicken_bacon', 'cheese_baguette', 'quiche', 'penne', 'noodle_soup']
    afternoon = ['pilsner', 'red_wine', 'white_wine', 'prosecco', 'penne', 'couscous']
    dinner = ['panini', 'chicken_bacon', 'cheese_baguette', 'quiche', 'penne', 'tapas', 'pilsner', 'red_wine', 'white_wine', 'prosecco', 'birell', 'cricri', 'pringles', 'olives', 'peanuts']
    evening = ['panini', 'chicken_bacon', 'cheese_baguette', 'quiche', 'penne', 'tapas']
    night = ['pilsner', 'red_wine', 'white_wine', 'prosecco', 'vodka', 'jameson', 'becherovka', 'ripe_pear', 'schweppes']

    if product in morning and daytime == "Breakfast":
        daytime_coefficient = 1.3
    elif product in late_morning and daytime == "Noon":
        daytime_coefficient = 1.2
    elif product in lunch and daytime == "Lunch":
        daytime_coefficient = 1.3
    elif product in afternoon and daytime == "Afternoon":
        daytime_coefficient = 1.2
    elif product in dinner and daytime == "Dinner":
        daytime_coefficient = 1.3
    elif product in evening and daytime == "Evening":
        daytime_coefficient = 1.2
    elif product in night and daytime == "Night":
        daytime_coefficient = 1.3

    elif product in morning and daytime == "Night":
        daytime_coefficient = 0.8
    elif product in morning and daytime == "Evening":
        daytime_coefficient = 0.9
    elif product in night and daytime == "Breakfast":
        daytime_coefficient = 0.6
    elif product in evening and daytime == "Breakfast":
        daytime_coefficient = 0.7

    else:
        daytime_coefficient = 1

    return daytime_coefficient
