class Num:
    def __init__(self, type_bill):
        self.type_bill = type_bill

    def bill(self):
        try:
            type_num = input('Enter the numbers to play:')
            type_num = type_num.split()
            check = []
            if len(type_num) > 10:
                print('More then 10 numbers entered, retry')
                type_num = Num.bill(self)
            for x in type_num:
                check.append(x)
                if int(x) < 0 or int(x) > 90:
                    print('One or more entered number are invalid, retry')
                    type_num = Num.bill(self)
            for y in check:
                check.remove(y)
                if y in check:
                    print('Double number revealed, retry')
                    type_num = Num.bill(self)
            if self == 'cinquina' and len(type_num) < 5:
                print('You have to ask at least for 5 numbers in order to play for a cinquina')
                type_num = Num.bill(self)
            elif self == 'quaterna' and len(type_num) < 4:
                print('You have to ask at least for 4 numbers in order to play for a quaterna')
                type_num = Num.bill(self)
            elif self == 'terno' and len(type_num) < 3:
                print('You have to ask at least for 3 numbers in order to play for a terno')
                type_num = Num.bill(self)
            elif self == 'ambo' and len(type_num) < 2:
                print('You have to ask at least for 2 numbers in order to play for an ambo')
                type_num = Num.bill(self)
            if len(type_num) == 0:
                Num.bill(self)

            return type_num

        except ValueError:
            print('Invalid argument, retry:')
            type_num = Num.bill(self)
            return type_num