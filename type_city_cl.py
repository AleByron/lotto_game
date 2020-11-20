class City:

    def __init__(self, type_city):
        self.typebb = type_city

    def cit(self, type_city):
        cities = ['bari', 'cagliari', 'firenze', 'genova', 'milano', 'napoli', 'palermo', 'roma', 'torino', 'venezia',
                  'all']

        city = type_city.lower()
        if city not in cities:
            type_city = ''
            print('Invalid city, retry.')
            type_city = City.cit(self, type_city)

        return type_city