import sys
import csv
from math import pi, sin, cos, acos
import os
import csv
from Airport import *


class AirportAtlas:
    """ class to hold information on all airports """


    def __init__(self, airport_csv):
        self.airport_dict = {}
        self.load_data(airport_csv)

    def load_data(self, airport_csv):
        """ method to read from csv file & create an airport dictionary """

        # open filename, read into 'f' using utf-8
        with open(os.path.join("input", airport_csv), "rt", encoding="utf8") as f:

            # assign read data to reader
            reader = csv.reader(f)

            # loop through data line-by-line
            for line in reader:

                # create an instance/object of Airport for each line
                airport = Airport(line[0], line[1], line[2], line[3], line[4], line[5])

                # assign line values to airport variables
                airport.iata = line[0]
                airport.airport_name = line[1]
                airport.lat = line[2]
                airport.long = line[3]
                airport.currency = line[4]
                airport.fuel = line[5]

                # assign 'iata' value as dictionary key for airport object
                self.airport_dict[airport.iata] = airport

        return self.airport_dict

    def get_dist_between_airports(self, iata1, iata2):
        """ method that returns the distance between two airports in kilometres """

        # retrieve airport objects using iata key
        airport1 = self.get_airport(iata1)
        airport2 = self.get_airport(iata2)

        # access lat, long values from airport objects
        lat1 = airport1.lat
        long1 = airport1.long
        lat2 = airport2.lat
        long2 = airport2.long

        # invoke get_circle_dist, assign result to distance
        distance = self.get_circle_dist(lat1, long1, lat2, long2)
        return distance


    def get_airport(self):
        """ method to take IATA code as argument & return corresponding airport object """

        return self.airport_dict

    @staticmethod
    def get_circle_dist(lat1, long1, lat2, long2):
        """ method that will calculate the distance between two points from lat/long coordinates """

        radius_earth = 6371  # in kilometres
        theta1 = long1 * (2 * pi) / 360
        theta2 = long2 * (2 * pi) / 360
        phi1 = (90 - lat1) * (2 * pi) / 360
        phi2 = (90 - lat2) * (2 * pi) / 360
        distance = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * radius_earth

        return distance

# print("Circle Distance Test: ", AirportAtlas.get_circle_dist(53.421333, -6.270075, 51.4775, -0.461389))