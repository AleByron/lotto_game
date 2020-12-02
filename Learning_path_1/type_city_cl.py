class City:

    def __init__(self, type_city):
        self.type_city = type_city

    def cit(self):
        cities = ['bari', 'cagliari', 'firenze', 'genova', 'milano', 'napoli', 'palermo', 'roma', 'torino', 'venezia',
                  'all']

        city = self.type_city.lower()
        if city not in cities:
            type_city = ''
            self.type_city=input('Invalid city, retry.')
            City.cit(self)

        return self.type_city