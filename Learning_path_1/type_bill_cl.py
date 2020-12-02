class typeb:

    def __init__(self, type_inp):
        self.type_inp = type_inp

    def type_bill(self):

        try:
            checkType = ['ambata', 'ambo', 'terno', 'quaterna', 'cinquina']
            self.type_inp = self.type_inp.lower()
            if self.type_inp not in checkType:
                self.type_inp = input('Your bill is invalid, retry: ')
                typeb.type_bill(self)
            return self.type_inp
        except EOFError:
            typeb.type_bill(self)
            return self.type_inp