import csv


def airport(destination_icao):
    csv_file = csv.reader(open('C:\development\AirlineOptimizer-TVS\AirlineOptimizer\AirlineOptimizer\helpers\data\icao_iata.csv', 'r'))

    # find the value in the relevant csv and return an IATA code
    for row in csv_file:
        if destination_icao in row[0]:
            iata = ''.join(row)
            iata = iata[5:8]
    return iata