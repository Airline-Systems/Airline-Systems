import csv

def IataToCountry(destination_iata):
    csv_file = csv.reader(open('data/helpers/iata_to_country.csv', 'r'))

    # find the value in the relevant csv and return a country
    for row in csv_file:
        if destination_iata in row[0]:
            country = ''.join(row)
            country = country[4:]
            print(country)
            return country

