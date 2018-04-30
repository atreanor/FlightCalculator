from AirportAtlas import *

import unittest
from Itinerary import *


class TestItinerary(unittest.TestCase):
    """ class to test Aircraft methods """

    def test1(self):
        """ test the correct number of inputs have been received """

        test_csv = '/home/alan/PycharmProjects/routeCalc/data/test_data.csv'
        itinerary = Itinerary()
        itinerary.load_itinerary(test_csv)
        self.assertTrue(len(itinerary.route) % 6 == 0)


if __name__ == '__main__':
    unittest.main()
