class check_winner:
    def __init__(self, numbs, tickets):
        self.numb = numbs
        self.ticket = tickets

    def checker(self,numbs,tickets):

        winners = []
        win_mess_arr = []
        won_ticket_bills = []

        for ticket in tickets:
            won_bills = {}
            win_mess = ''
            mess = ''
            ambata = 0
            ambo = 0
            terno = 0
            quaterna = 0
            cinquina = 0
            n = 0 # to keep count of bills (distinguish rome from "all" and rome from "rome" in won bills)

            win = True
            x = 0 #To access key related to the ticket's bill
            while len(ticket) > x:
                this_ticket_bill = ticket["Bill" + str(x)[0][0]]
                for city in numbs:
                    if city == this_ticket_bill[2] and city != 'all':
                        numb = numbs[city]



                if this_ticket_bill[2] == 'all':
                    for city in numbs:
                        score = 0
                        numb = numbs[city]
                        for n in ticket["Bill" + str(x)][1]:
                            if int(n) in numb:
                                score = score + 1
                        bills_amount = 0
                        if this_ticket_bill[0] == "ambo" and score >= 2:
                            win = True
                            bills_amount = score - 1
                            ambo = ambo + bills_amount
                        elif this_ticket_bill[0] == "terno" and score >= 3:
                            win = True
                            bills_amount = score - 2
                            terno = terno + bills_amount
                        elif this_ticket_bill[0] == "quaterna" and score >= 4:
                            win = True
                            bills_amount = score - 3
                            quaterna = quaterna + bills_amount
                        elif this_ticket_bill[0] == "cinquina" and score >= 5:
                            win = True
                            bills_amount = score - 4
                            cinquina = cinquina + bills_amount
                        elif this_ticket_bill[0] == "ambata" and score >= 1:
                            win = True
                            bills_amount = score
                            ambata = ambata + bills_amount
                        else:
                            win = False

                        if win == True:
                            won_bills[city + str(n)]=[this_ticket_bill[0],bills_amount, len(this_ticket_bill[1])]
                            win = True

                else:
                    score = 0
                    for n in ticket["Bill" + str(x)][1]:
                        if int(n) in numb:
                            score = score + 1

                    bills_amount = 0
                    if this_ticket_bill[0] == "ambo" and score >= 2:
                        win = True
                        bills_amount = score - 1
                        ambo = ambo + bills_amount
                    elif this_ticket_bill[0] == "terno" and score >= 3:
                        win = True
                        bills_amount = score - 2
                        terno = terno + bills_amount
                    elif this_ticket_bill[0] == "quaterna" and score >= 4:
                        win = True
                        bills_amount = score - 3
                        quaterna = quaterna + bills_amount
                    elif this_ticket_bill[0] == "cinquina" and score >= 5:
                        win = True
                        bills_amount = score - 4
                        cinquina = cinquina + bills_amount
                    elif this_ticket_bill[0] == "ambata" and score >= 1:
                        win = True
                        bills_amount = score
                        ambata = ambata + bills_amount
                    else:
                        win = False

                    if win == True:
                        won_bills[this_ticket_bill[2] + str(n)] = [this_ticket_bill[0], bills_amount, len(this_ticket_bill[1])]
                        win = True



                x = int(x)
                x = x + 1

                if win == True and ticket not in winners:
                    winners.append(ticket)



            if winners != []:
                win_mess = "In this ticket you won: \n Ambate : {ambt} \n Ambi :  {amb} \n Terni : {ter} \n Quaterne : {quat} \n Cinquine : {cinq} ".format(ambt=ambata, amb = ambo, ter = terno, quat = quaterna, cinq = cinquina)
                win_mess_arr.append(win_mess)
            won_ticket_bills.append(won_bills)


        return winners, win_mess_arr, won_ticket_bills
