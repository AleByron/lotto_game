from LP1 import Ticket
from LP1 import arg_error
from Learning_path_1.type_print import prnt
import argparse
from learning_path_2.extract import extraction
from learning_path_2.winners import check_winner

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