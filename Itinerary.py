from main import *
import csv
import os
import itertools


class Itinerary:
    """ class to represent itinerary of each journey & calculate the most efficient path """

    def __init__(self, airport_dict, aircraft_dict):
        """ class constructor - initialises input & dictionary """

        self.iata1 = None
        self.iata2 = None
        self.iata3 = None
        self.iata4 = None
        self.iata5 = None
        self.range = None
        self.code = None
        self.route = []
        self.airport_dict = airport_dict
        self.aircraft_dict = aircraft_dict

    def load_itinerary(self, input_csv):
        """ method to input each intinerary from csvFile into a list """

        # open filename, read into 'f' using utf-8
        with open(os.path.join("input", input_csv), "rt", encoding="utf8") as f:

            # assign read data to reader
            reader = csv.reader(f)
            # loop through data line-by-line
            for line in reader:

                try:
                    self.iata1 = line[0]
                    self.iata2 = line[1]
                    self.iata3 = line[2]
                    self.iata4 = line[3]
                    self.iata5 = line[4]
                    self.code = line[5]

                    # retrieve aircraft range from dictionary & print to console
                    self.range = self.aircraft_dict[self.code].get_range()
                    print("Aircraft range: ", self.range)

                    # produce a list of tuples with all permutations for the destinations 2, 3, 4, & 5
                    # destination 1 will be appended to start  & finish of permutations
                    permutations_all = self.route_permutations(self.iata2, self.iata3, self.iata4, self.iata5)
                    permutation_by_cost_dict = {}
                    for permutation in permutations_all:
                        path = [self.iata1]
                        path.extend(list(permutation))
                        path.append(self.iata1)

                        cost_overall = 0  # keep track of the overall cost of the path

                        path_queue = path[::-1]  # Create a duplicate of the path as queue
                        failed = False
                        while len(path_queue) > 1:
                            airport_from = path_queue.pop()
                            airport_to = path_queue[-1]
                            airport_from_obj = self.airport_dict[airport_from]
                            airport_to_obj = self.airport_dict[airport_to]
                            # calculate distance between airports
                            distance = AirportAtlas.get_circle_dist(airport_from_obj.get_lat(),
                                                                    airport_from_obj.get_long(),
                                                                    airport_to_obj.get_lat(),
                                                                    airport_to_obj.get_long())
                            # calculate cost of trip, distance * local fuel price
                            cost = distance * float(self.airport_dict[airport_from].get_fuel())
                            # test to make sure aircraft range can cover trip
                            if distance > float(self.aircraft_dict[self.code].range):
                                print('** ALERT: aircraft range cannot cover distance from', airport_from,
                                      'to', airport_to)
                                failed = True
                                cost_overall = 0
                                break
                            else:
                                cost_overall += cost

                        if not failed:
                            # valid trip values added to total trip value
                            permutation_by_cost_dict[cost_overall] = path

                    this_route = ', '.join(line)
                    if len(permutation_by_cost_dict) == 0:
                        print('*' * 100)
                        print('No path was found for ', this_route)
                        print('*' * 100)
                        print()
                    else:
                        minimum_cost = min(permutation_by_cost_dict.keys())
                        if minimum_cost == 0:
                            from pprint import pprint
                            pprint(permutation_by_cost_dict.items())
                        cheapest_path = permutation_by_cost_dict[minimum_cost]

                        print('*'*100)
                        print('Cheapest path of ', this_route, 'is ', cheapest_path, 'with cost: ', minimum_cost)
                        print('*'*100)
                        print()

                except KeyError as e:
                    print('ERROR: Could not find airport with IATA code: ', e)
        print()
        print('Thank you for using Flight Path Calculator - SAFE TRAVELS!')

    def route_permutations(self, iata2, iata3, iata4, iata5):
        """ method to produce a list of permutations of 4 inputs """

        route_perm = list(itertools.permutations([iata2, iata3, iata4, iata5]))
        return route_perm
