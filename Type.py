class typeb:

    def type_bill(self):
        checkType = ['ambata', 'ambo', 'terno', 'quaterna', 'cinquina']
        typebb = input('What type of bill you want to play?(ambata, ambo, terno, quaterna, cinquina):')
        typebb = typebb.lower()
        if typebb not in checkType:
            print('Your bill is invalid, retry')
            typebb = typeb.type_bill(self)
        return typebb