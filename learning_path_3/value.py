class value:
    def __init__(self, ticket):
        self.ticket = ticket


    def calculate_value(self,ticket):

        final_value = 0
        for won_bill in ticket:
            if ticket[won_bill][0] == "ambata":
                bill_values = [11.23,5.61,3.74,2.80,2.24,1.87,1.60,1.40,1.24,1.12]
                final_value = final_value + ticket[won_bill][1]*bill_values[ticket[won_bill][2]-1]
            elif ticket[won_bill][0] == 'ambo':
                bill_values = [250,83.33,41.66,25,16.66,11.90,8.92,6.94,5.55]
                final_value = final_value + ticket[won_bill][1]*bill_values[ticket[won_bill][2]-2]
            elif ticket[won_bill][0] == 'terno':
                bill_values = [4500,1125,450,225,128.57,80.35,53.57,37.50]
                final_value = final_value + ticket[won_bill][1]*bill_values[ticket[won_bill][2]-3]
            elif ticket[won_bill][0] == 'quaterna':
                bill_values = [120000,24000,8000,3428.57,1714.28,952.38,571.42]
                final_value = final_value + ticket[won_bill][1]*bill_values[ticket[won_bill][2]-4]
            elif ticket[won_bill][0] == 'cinquina':
                bill_values = [6000000,1000000,285714.28,107142.85,47619.04,23809.52]
                final_value = final_value + ticket[won_bill][1]*bill_values[ticket[won_bill][2]-5]

        final_value_taxed = final_value - (final_value/100)*8

        return final_value, final_value_taxed


