import sys
from Type import typeb
from City import City
from Num import Num

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
                typebill = typeb.type_bill(self.args)
                type_num = Num.bill(typebill)
                city = City.cit(self.args)
                bills.setdefault('Bill' + str(x), [])
                bills['Bill' + str(x)].append(typebill)
                bills['Bill' + str(x)].append(type_num)
                bills['Bill' + str(x)].append(city)
                x = x + 1

        ticket = '+'+'-'*29+'+'+'-'*58+'+'+'-'*29+'+'+'\n'
        for bill in bills:
            cell00 = int(15-(len(bills[bill][0])/2))
            cell01 = int(14-(len(bills[bill][0])/2))
            if len(bills[bill][0])%2 != 0 :
                cell00 = int(15-(len(bills[bill][0])/2))
                cell01 = int(15-(len(bills[bill][0])/2))
            cell10 = int(30-(len(str(bills[bill][1]))/2))
            cell11 = int(30-(len(str(bills[bill][1]))/2))
            if cell10 + cell11 + len(str(bills[bill][1]))/2 != 58:
                cell11 = 60 - cell10 - len(str(bills[bill][1]))
            cell20 = int(15-(len(bills[bill][2])/2))
            cell21 = int(14-(len(bills[bill][2])/2))
            if cell10 + cell11 + len(str(bills[bill][1]))/2 != 29:
                cell21 = 29 - cell20 - len(str(bills[bill][2]))
            ticket = ticket+ '|' + ' '*cell00 + bills[bill][0] + ' '*cell01
            ticket = ticket+ '|' + ' '*cell10 + str(bills[bill][1])[1:len(bill[1])-2] + ' '*cell11
            ticket = ticket+ '|' + ' '*cell20 + bills[bill][2] + ' '*cell21 + '|' + '\n'
            ticket = ticket + '+'+'-'*29+'+'+'-'*58+'+'+'-'*29+'+'+'\n'
        return ticket




def main():
    try:
        bill = sys.argv[1]
        t = Ticket(bill)
        print(t.Finalticket())
    except IndexError:
        print('Invalid argument, retry')


main()

