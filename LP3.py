import argparse
from learning_path_2.extract import extraction
from learning_path_2.winners import check_winner
from Learning_path_1.type_bill_cl import typeb
from Learning_path_1.type_city_cl import City
from Learning_path_1.type_num_cl import Num
from learning_path_3.type_print2 import prnt
from learning_path_3.value import value

class arg_error1(Exception):
    print('error, invalid argument')
    #quit()

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
                money_amount = float(input('How much do you want to bet?: '))
                bills.setdefault('Bill' + str(x), [])
                bills['Bill' + str(x)].append(typebill)
                bills['Bill' + str(x)].append(type_num)
                bills['Bill' + str(x)].append(type_city)
                bills['Bill' + str(x)].append(money_amount)

                x = x + 1

        return bills

def main():
    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('inp', metavar='N', type=int)
        args = parser.parse_args()
        print(args.inp)

        if int(args.inp) > 5:
            raise arg_error1
        elif int(args.inp) < 1:
            raise arg_error1

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
        print(extr)
        the_winners = check_winner(extr, all_tickets)
        winners = the_winners.checker(extr, all_tickets)
        #print(winners[2])
        c = 0 #counter for win messages
        if winners[0] != []:
            for tick in winners[0]:

                ticket_obj = prnt(tick)
                print(ticket_obj.lotto_ticket(tick))
                print(winners[1][c])
                money_obj = value(winners[2][c])
                money = money_obj.calculate_value(winners[2][c])
                print("You're lucky! You just won {cash}, the import out of taxes is {taxed_cash}".format(cash=round(money[0],2), taxed_cash=round(money[1],2)))
                c = c+1
                print('\n')
        quit()
    except IndexError:
        print('Invalid argument, retry')

main()