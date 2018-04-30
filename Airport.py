
class Airport:
    """ a class to store Airport objects """

    def __init__(self, iata, name, lat, long, currency, fuel):
        """ class constructor initialises variables with input """

        # print('--- Airport Class Constructor ---')
        self.iata = iata
        self.name = name
        self.lat = lat
        self.long = long
        self.currency = currency
        self.fuel = fuel
        # print('iata: ', iata, ' name: ', name)

    def get_lat(self):
        """ method to retrieve Latitude """
        return float(self.lat)

    def get_long(self):
        """ method to retrieve Longitude """
        return float(self.long)

    def get_fuel(self):
        """ method to retrieve local fuel price """
        return self.fuel

    def __str__(self):
        """ string method to return a descriptive output """

        return str("IATA: " + self.iata + ", AirportName: " + self.name + ", Lat: " + self.lat
                   + ", Long: " + self.long + " , Currency: " + self.currency + " Fuel: " + self.fuel)
