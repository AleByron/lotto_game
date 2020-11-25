import argparse

from Learning_path_1.type_print import prnt
from Learning_path_1.type_ticket_cl import Ticket

class arg_error(Exception):
    pass

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

