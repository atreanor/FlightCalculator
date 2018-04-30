from AirportAtlas import *

import unittest
from Aircraft import *


class TestAirportAtlas(unittest.TestCase):
    """ class to test Aircraft methods """

    test_csv = '/home/alan/PycharmProjects/routeCalc/data/test_data.csv'
    airport_atlas = AirportAtlas(test_csv)

    def test1(self):
        lat1 = 53.421333
        long1 = -6.270075
        lat2 = 51.4775
        long2 = -0.461389
        self.assertTrue(AirportAtlas.get_circle_dist(lat1, long1, lat2, long2) == 448.8922295538067)

    # def test2(self):
    #     self.assertTrue(airport_atlas.get_airport(DUB))


if __name__ == '__main__':
    unittest.main()
