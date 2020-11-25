import argparse
from learning_path_2.extract import extraction
from learning_path_2.winners import check_winner
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

        n_bill = args.inp
        all_tickets = []
        while True:
            if n_bill==0:
                check = input('Do you want to enter another ticket?(Press any key to continue):')
                if check == '':
                    break
                else:
                    n_bill = input('How many bills in this ticket?:')
                    while n_bill.isdigit() != True:
                        n_bill = input('You should enter an integer:')
            n_bill  = int(n_bill)
            t = Ticket(n_bill)
            ticket = t.Finalticket()
            all_tickets.append(ticket)
            n_bill = 0


        extract = extraction()
        extr = extract.numbers()
        the_winners = check_winner(extr, all_tickets)
        #print(the_winners.checker(extr, all_tickets ))
        winners = the_winners.checker(extr, all_tickets )
        for tick in winners:
            ticket_obj = prnt(tick)
            print(ticket_obj.lotto_ticket(tick))
            print('\n')

    except IndexError:
        print('Invalid argument, retry')

    except arg_error:
        pass

main()