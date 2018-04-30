
class Aircraft:
    """ a class to store Airport objects """

    def __init__(self, code, units, range):
        """ class constructor initialises variables with input """

        self.code = code
        self.units = units
        self.range = range

    def get_range(self):
        """ method to retrieve aircraft range """

        return self.range

    def __str__(self):
        """ string method to return a descriptive output """

        return str("Aircraft Code: " + self.code + " Units: " + self.units + " range: " + self.range)
