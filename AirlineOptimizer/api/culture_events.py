import yaml, os
from predicthq import Client
from datetime import datetime, timedelta


def CultureEventOrigin(origin):
    yaml_file = open('config_files/configurator.yaml')
    configurator = yaml.load(yaml_file, Loader=yaml.FullLoader)
    access_token = os.environ.get('PREDICTHQ_CLIENT_KEY')
    phq = Client(access_token)

    start = {
        'gte': datetime.today().strftime('%Y-%m-%d'),
        'lte': datetime.today() + timedelta(7)
    }
    for event in phq.events.search(place={'scope': origin}, aviation_rank_level = [2,5], start=start):  # airport code
        event_rank = event.aviation_rank
        event_category = event.category
        event_name = event.title
        event_date = event.start.strftime('%Y-%m-%d')

        if event_rank == 2:
            event_coefficient = float(str(configurator['rank2_event']))
        elif event_rank == 3:
            event_coefficient = float(str(configurator['rank3_event']))
        elif event_rank == 4:
            event_coefficient = float(str(configurator['rank4_event']))
        elif event_rank == 5:
            event_coefficient = float(str(configurator['rank5_event']))
        else:
            event_coefficient = 1
        try:
            culture_event = [event_coefficient, event_category, event_name, event_date]
        except:
            culture_event = [1, 'no category', 'no name', 'no date']
        return culture_event


def CultureEventDestination(destination):
    yaml_file = open('config_files/configurator.yaml')
    configurator = yaml.load(yaml_file, Loader=yaml.FullLoader)
    phq = Client(access_token='2xX70l0o8KoDXIpVbFdQY1GSWLUCWOi2R3ACH-QJ_ftM-9GS5MdPWQl')
    start = {
        'gte': datetime.today().strftime('%Y-%m-%d'),
        'lte': datetime.today() + timedelta(7),
    }
    for event in phq.events.search(place={'scope': destination}, aviation_rank_level = [2,5], start=start):  # airport code
        event_rank = event.aviation_rank
        event_category = event.category
        event_name = event.title
        event_date = event.start.strftime('%Y-%m-%d')

        if event_rank == 2:
            event_coefficient = float(str(configurator['rank2_event']))
        elif event_rank == 3:
            event_coefficient = float(str(configurator['rank3_event']))
        elif event_rank == 4:
            event_coefficient = float(str(configurator['rank4_event']))
        elif event_rank == 5:
            event_coefficient = float(str(configurator['rank5_event']))
        else:
            event_coefficient = 1
        try:
            culture_event = [event_coefficient, event_category, event_name, event_date]
        except:
            culture_event = [1, 'no category', 'no name', 'no date']

        return culture_event



