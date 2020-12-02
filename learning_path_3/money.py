class money:

    def calculate_money(self):
        try:
            money_amount = float(input('The entered amount is invalid, retry: '))
        except ValueError:
            money_amount = money.calculate_money(self)

        return money_amount