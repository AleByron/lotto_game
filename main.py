import random
def type_bill():
    checkType = ['ambata', 'ambo', 'terno', 'quaterna', 'cinquina']
    type = input('What type of bill you want to play?(ambata, ambo, terno, quaterna, cinquina):')
    type = type.lower()
    if type not in checkType:
        print('Your bill is invalid, retry')
        type = type_bill()
    return type


def cit():
    cities = ['bari', 'cagliari', 'firenze', 'genova', 'milano', 'napoli', 'palermo', 'roma', 'torino', 'venezia','all']
    city = input('On wich city you want to play?\n(Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia or all):')
    city = city.lower()
    city_arr = []
    city = city.split()
    for x in city:
        if x not in cities:
            city_arr = []
            print('One of the entered cities is invalid, retry.')
            city_arr.append(cit())
        else:
            city_arr.append(x)
    return city_arr

def bill(type):

    type_num = input('How many numbers you want to play?(From 1 up to 10):')
    if type == 'cinquina' and type_num < '5':
        type_num = input('You have to ask at least for 5 numbers in order to play for a cinquina, how many number you want to play?:')
        if type_num < '5':
            bill(type)
    elif type == 'quaterna' and type_num < '4':
        type_num = input(
            'You have to ask at least for 4 numbers in order to play for a quaterna, how many number you want to play?:')
        if type_num < '4':
            bill(type)
    elif type == 'terno' and type_num < '3':
        type_num = input(
            'You have to ask at least for 3 numbers in order to play for a terno, how many number you want to play?:')
        if type_num < '3':
            bill(type)
    elif type == 'ambo' and type_num < '2':
        type_num = input(
            'You have to ask at least for 2 numbers in order to play for an ambo, how many number you want to play?:')
        if type_num < '2':
            bill(type)
    if type_num == '0':
        bill(type)

    return type_num

def lottoticket():
    num = int(input('How many bills you want to play?(Max 5):'))
    bills = {}
    if num == 0:
        return
    elif 1 <= num <=5:
        x = 0
        while x < num:
            type = type_bill()
            type_num = bill(type)
            city = cit()
            bills.setdefault('Bill' + str(x), [])
            bills['Bill' + str(x)].append(type)
            bills['Bill' + str(x)].append(type_num)
            bills['Bill' + str(x)].append(city)
            x = x + 1
    return bills

def main():
    print(lottoticket())


if __name__ == "__main__":
        main()