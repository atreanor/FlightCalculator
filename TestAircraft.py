import unittest
from Aircraft import *


class TestAircraft(unittest.TestCase):
    """ class to test Aircraft methods"""

    def test1(self):
        code = 'MD11'
        units = 'metric'
        range = 20272
        a1 = Aircraft(code, units, range)
        self.assertTrue(a1.get_range() == 20272)


if __name__ == '__main__':
    unittest.main()

