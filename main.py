from AirportAtlas import *
from AircraftFleet import *
from Itinerary import *


def main():
    """ main method that is entry point for program """

    print("Welcome to the Flight Path Calculator!")
    print()
    # append absolute file path below for newAirport.csv on local instance
    airport_csv = "/home/FlightCalculator/data/newAirport.csv"
    new_atlas = AirportAtlas(airport_csv)
    # append absolute file path below for newAircraft.csv on local instance
    aircraft_csv = "/home/FlightCalculator/data/newAircraft.csv"
    new_fleet = AircraftFleet(aircraft_csv)
    input_csv = input("Enter a CSV file with required parameters: ")
    new_itinerary = Itinerary(new_atlas.airport_dict, new_fleet.aircraft_dict)
    new_itinerary.load_itinerary(input_csv)


if __name__ == '__main__':
    main()
