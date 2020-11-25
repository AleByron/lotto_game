class check_winner:
    def __init__(self, numbs, tickets):
        self.numb = numbs
        self.ticket = tickets

    def checker(self,numbs,tickets):

        winners = []

        for ticket in tickets:
            win = True
            x = 0 #To access key related to the ticket's bill
            while len(ticket) > x:
                this_ticket_bill = ticket["Bill" + str(x)[0][0]]
                for city in numbs:
                    if city == this_ticket_bill[2]:
                        numb = numbs[city]

                score = 0
                for n in ticket["Bill" + str(x)][1]:
                    if int(n) in numb:
                        score = score + 1


                if this_ticket_bill[0] == "ambo" and score >= 2:
                    win = True
                elif this_ticket_bill[0] == "terno" and score >= 3:
                    win = True
                elif this_ticket_bill[0] == "quaterna" and score >= 4:
                    win = True
                elif this_ticket_bill[0] == "cinquina" and score >= 5:
                    win = True
                elif this_ticket_bill[0] == "ambata" and score >= 1:
                    win = True
                else:
                    win = False


                x = int(x)
                x = x + 1

                if win == True and ticket not in winners:
                    winners.append(ticket)


        return winners
