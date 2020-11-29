import random

class extraction:
    def numbers(self):
        numbs = {'bari':[], 'cagliari':[], 'firenze':[], 'genova':[], 'milano':[], 'napoli':[], 'palermo':[], 'roma':[], 'torino':[], 'venezia':[]}
        for city in numbs:
            x = 0
            while x < 10:
                n = random.randint(1, 90)
                if n not in numbs[city]:
                    numbs[city].append(n)
                    x = x + 1
                else:
                    pass
        return numbs