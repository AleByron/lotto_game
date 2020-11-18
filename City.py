class City:
    def cit(self):
        cities = ['bari', 'cagliari', 'firenze', 'genova', 'milano', 'napoli', 'palermo', 'roma', 'torino', 'venezia',
                  'all']
        city = str(input(
            'On wich city you want to play?\n(Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia or all):'))
        city = city.lower()
        if city not in cities:
            city = ''
            print('Invalid city, retry.')
            city = City.cit(self)

        return city