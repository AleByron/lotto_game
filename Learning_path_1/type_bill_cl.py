class typeb:

    def __init__(self, type_inp):
        self.typebb = type_inp

    def type_bill(self, type_inp):

        try:
            checkType = ['ambata', 'ambo', 'terno', 'quaterna', 'cinquina']
            type_inp = type_inp.lower()
            if type_inp not in checkType:
                type_inp = input('Your bill is invalid, retry: ')
                typeb.type_bill(self, type_inp)
            return type_inp
        except EOFError:
            typeb.type_bill(self, type_inp)
            return type_inp