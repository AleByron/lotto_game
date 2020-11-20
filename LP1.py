import argparse
import os
from Learning_path_1.type_bill_cl import typeb
from Learning_path_1.type_city_cl import City
from Learning_path_1.type_num_cl import Num
from Learning_path_1.type_print import prnt

class arg_error(Exception):
    pass

class Ticket:
    def __init__(self, args):
        self.args = args

    def Finalticket(self):
        bills = {}
        args = int(self.args)
        if args <= 0:
            print('Invalid bills number, retry')
            return
        elif 1 <= args <= 5:
            x = 0
            while x < args:
                type_inp = input('What type of bill you want to play?(ambata, ambo, terno, quaterna, cinquina):')
                typebill = typeb.type_bill(self.args, type_inp)
                type_num = Num.bill(self.args, typebill)
                city = str(input('On wich city you want to play?\n(Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia or all):'))
                type_city = City.cit(self.args,city)
                bills.setdefault('Bill' + str(x), [])
                bills['Bill' + str(x)].append(typebill)
                bills['Bill' + str(x)].append(type_num)
                bills['Bill' + str(x)].append(type_city)
                x = x + 1

        return bills




def main():
    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('inp', metavar='N', type=int)
        args = parser.parse_args()
        if args.inp > 5:
            raise arg_error
        elif args.inp < 1:
            raise arg_error


        t = Ticket(args.inp)
        fin_ticket = t.Finalticket()
        ticket_obj = prnt(fin_ticket)
        print(ticket_obj.lotto_ticket(fin_ticket))

    except IndexError:
        print('Invalid argument, retry')

    except arg_error:
        print('Invalid argument, retry')
        quit()

if __name__ == "__main__":
    main()

