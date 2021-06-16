import requests
import yaml

yaml_file = open('configurator.yaml')
configurator = yaml.load(yaml_file, Loader=yaml.FullLoader)

#NEEEEDS ATTENTION!!!!!!!!!!!

response = requests.get("https://holidays.abstractapi.com/v1?api_key=1c9853c08639453482f59167a222451d&country=CZ&year=2021&month=12&day=24")

holiday = 0
public_holiday_coeficient = 0
if holiday == 1:
    public_holiday_coeficient = configurator['public_holiday_in_origin']
    public_holiday_code = "public holiday in origin"
else:
    public_holiday_coeficient = configurator['public_holiday_in_destination']
    public_holiday_code = "no public holiday in origin"
