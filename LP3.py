import argparse
from learning_path_2.extract import extraction
from learning_path_2.winners import check_winner
from Learning_path_1.type_bill_cl import typeb
from Learning_path_1.type_city_cl import City
from Learning_path_1.type_num_cl import Num
from learning_path_3.type_print2 import prnt
from learning_path_3.value import value
from learning_path_3.money import money

class Ticket:
    def __init__(self, args):
        self.args = args

    def Finalticket(self):
        bills = {}
        args = int(self.args)
        if self.args <= 0:
            print('Invalid bills number, retry')
            return
        elif 1 <= args <= 5:
            x = 0
            while x < args:
                type_inp = typeb(input('What type of bill you want to play?(ambata, ambo, terno, quaterna, cinquina):'))
                typebill = typeb.type_bill(type_inp)
                type_num = Num.bill(typebill)
                city = City(str(input('On wich city you want to play?\n(Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia or all):')))
                type_city = City.cit(city)
                try:
                    money_amount = float(input('How much do you want to bet?: '))
                except ValueError:
                    money_amount = money.calculate_money(self.args)
                print(money_amount)
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
            print('You can enter a maximum of 5 bills for a ticket')
            quit()
        elif int(args.inp) < 1:
            print('You should enter at least a single  bill for a ticket')
            quit()
        else:
            pass

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
        winners = the_winners.checker()
        c = 0 #counter for win messages
        if winners[1] != ['In this ticket you won: \n Ambate : 0 \n Ambi :  0 \n Terni : 0 \n Quaterne : 0 \n Cinquine : 0 ']:
            for tick in winners[0]:
                ticket_obj = prnt(tick)
                print(ticket_obj.lotto_ticket())
                print(winners[1][c])
                money_obj = value(winners[2][c])
                print(winners)
                money = money_obj.calculate_value()
                print(money)
                print("You're lucky! You just won {cash}, the import out of taxes is {taxed_cash}".format(cash=round(money[0],2), taxed_cash=round(money[1],2)))
                c = c+1
                print('\n')
        else:
            print('No winner ticket detected')
        quit()
    except IndexError:
        print('Invalid argument, retry')

if __name__ == "__main__":
        main()