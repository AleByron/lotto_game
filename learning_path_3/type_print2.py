class prnt:
    def __init__(self, bills):
        self.bills = bills

    def lotto_ticket(self):
        ticket = '+' + '-' * 29 + '+' + '-' * 58 + '+' + '-' * 29 + '+' + '-' * 29 + '+' + '\n'
        for bill in self.bills:
            cell00 = int(15 - (len(self.bills[bill][0]) / 2))
            cell01 = int(14 - (len(self.bills[bill][0]) / 2))
            if len(self.bills[bill][0]) % 2 != 0:
                cell00 = int(15 - (len(self.bills[bill][0]) / 2))
                cell01 = int(15 - (len(self.bills[bill][0]) / 2))
            cell10 = int(30 - (len(str(self.bills[bill][1])) / 2))
            cell11 = int(30 - (len(str(self.bills[bill][1])) / 2))
            if cell10 + cell11 + len(str(self.bills[bill][1])) / 2 != 58:
                cell11 = 60 - cell10 - len(str(self.bills[bill][1]))
            cell20 = int(15 - (len(self.bills[bill][2]) / 2))
            cell21 = int(14 - (len(self.bills[bill][2]) / 2))
            if cell10 + cell11 + len(str(self.bills[bill][1])) / 2 != 29:
                cell21 = 29 - cell20 - len(str(self.bills[bill][2]))
            cell30 = int(15 - (len(str(self.bills[bill][3])) / 2))
            cell31 = int(14 - (len(str(self.bills[bill][3])) / 2))
            if cell30 + cell31 + len(str(self.bills[bill][3])) / 2 != 29:
                cell31 = 29 - cell30 - len(str(self.bills[bill][3]))


            ticket = ticket + '|' + ' ' * cell00 + self.bills[bill][0] + ' ' * cell01
            ticket = ticket + '|' + ' ' * cell10 + str(self.bills[bill][1])[1:len(bill[1]) - 2] + ' ' * cell11
            ticket = ticket + '|' + ' ' * cell20 + self.bills[bill][2] + ' ' * cell21
            ticket = ticket + '|' + ' ' * cell30 + str(self.bills[bill][3]) + ' ' * cell31 + '|' + '\n'
            ticket = ticket + '+' + '-' * 29 + '+' + '-' * 58 + '+' + '-' * 29 + '+' + '-' * 29 + '+' + '\n'

        return ticket