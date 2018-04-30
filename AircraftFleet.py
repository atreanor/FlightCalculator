import os
import csv
from Aircraft import *


class AircraftFleet:
    """ a class to read aircraft from a csv file and create a dictionary """

    def __init__(self, aircraft_csv):
        """ class constructor initialises variables """

        self.aircraft_dict = {}
        self.read_aircraft(aircraft_csv)

    def read_aircraft(self, aircraft_csv):
        """ method to read aircraft data from csv file into dictionary """

        # open filename, read into 'f' using utf-8
        with open(os.path.join("input", aircraft_csv), "rt", encoding="utf8") as f:

            # assign read data to reader
            reader = csv.reader(f)

            # loop through data line-by-line
            for line in reader:

                # create an instance/object of Airport for each line
                aircraft = Aircraft(line[0], line[1], line[2])

                # assign line values to airport variables
                aircraft.code = line[0]
                aircraft.units = line[1]
                aircraft.range = line[2]

                # assign 'code' value as dictionary key for aircraft object
                self.aircraft_dict[aircraft.code] = aircraft

            return self.aircraft_dict


    def __str__(self):
        return "Aircraft fleet dictionary created"
