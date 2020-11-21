from LP1 import Ticket
from LP1 import arg_error
import argparse
import random


class extraction:
    def numbers(self):
        numbs = []
        x = 0
        while x < 10:
            n = random.randint(1, 90)
            if n not in numbs:
                numbs.append(n)
                x = x+1
            else:
                pass
        return numbs

class check_winner:
    def __init__(self, numb, tickets):
        self.numb = numb
        self.ticket = tickets

    def checker(self,numb,tickets):

        winners = []
        numb = [1,2,3,4,5,6,7,8,9,10]
        for ticket in tickets:
            win = True
            print(ticket)
            print('shit')
            x = 0 #To access key related to the ticket's bill
            while len(ticket) > x:
                score = 0
                print(len(ticket))
                for n in ticket["Bill" + str(x)][1]:
                    print(n)
                    if int(n) in numb:
                        score = score + 1
                        print('t')
                    else:
                        print('f')
                print('score =',score)
                print(ticket["Bill"+str(x)[0][0]])
                this_ticket_bill = ticket["Bill"+str(x)[0][0]]
                if this_ticket_bill[0] == "ambo" and score >= 2:
                    win = True
                elif this_ticket_bill[0] == "terno" and score >= 3:
                    win = True
                elif this_ticket_bill[0] == "quaterna" and score >= 4:
                    win = True
                elif this_ticket_bill[0] == "cinquina" and score >= 5:
                    win = True
                elif this_ticket_bill[0] == "ambata" and score >= 1:
                    win = True
                else:
                    win = False

                x = int(x)
                x = x + 1

                if win == True:
                    winners.append(ticket)


        return winners


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
        print(extr)
        print(all_tickets)
        the_winners = check_winner(extr, all_tickets)
        print(the_winners.checker(extr, all_tickets ))
    except IndexError:
        print('Invalid argument, retry')

    except arg_error:
        pass

main()