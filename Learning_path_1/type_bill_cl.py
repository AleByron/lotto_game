class typeb:

    def __init__(self, type_inp):
        self.typebb = type_inp

    def type_bill(self, type_inp):

        try:
            checkType = ['ambata', 'ambo', 'terno', 'quaterna', 'cinquina']
            type_inp = type_inp.lower()
            if type_inp not in checkType:
                print('Your bill is invalid, retry')
                type_inp = typeb.type_bill(self, type_inp)
            return type_inp
        except EOFError:
            type_inp = typeb.type_bill(self, type_inp)
            return type_inp