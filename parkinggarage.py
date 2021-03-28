from IPython.display import clear_output
class ParkingGarage():
    """
        Attributes for the class:
        - Ticket count as an integer
        - Parking space count as an integer
        - Dictionary that states currentTicket status
    """
    def __init__(self,tickets,parkingspaces,usedspaces,ticketstatus):
        self.tickets = tickets
        self.parkingspaces = parkingspaces
        self.usedspaces = usedspaces
        self.ticketstatus = ticketstatus

    def takeTicket(self):
        if self.tickets == 0:
            print(f"The parking deck is currently full. Sorry.")
        else:
            confirm = input("Are you sure you would like to take a ticket? (Yes/No) ")
            if confirm.lower() == "yes":
                print(self.parkingspaces)
                spaceselect = input("Please select a parking space from the previous list: ")
                if spaceselect in self.parkingspaces:
                    self.parkingspaces.remove(spaceselect)
                if spaceselect not in self.usedspaces:
                    self.usedspaces.append(spaceselect)
                self.ticketstatus[spaceselect] = 'unpaid'
                self.tickets -= 1
            elif confirm.lower() == "no":
                print(f"Have a nice day!")
            else:
                print(f"Please try again.")

    def payForParking(self):
        print(self.usedspaces)
        payforspace = input("From the previous list, what parking spot are you paying for? ")
        if payforspace in self.usedspaces:
            payment = input("Please enter 'Pay' to submit payment. ")
            if payment.lower() == 'pay':
                self.usedspaces.remove(payforspace)
                self.tickets += 1
                self.parkingspaces.append(payforspace)
                self.ticketstatus[payforspace] = 'paid'
                print(f"Thank you for your payment!")
        elif payforspace not in self.usedspaces:
            print(f"Error, please try again.")

    def leaveGarage(self):
        print(self.usedspaces)
        spacenum = input("What was your parking space number? ")
        if spacenum in self.ticketstatus:
            if self.ticketstatus[spacenum] == 'paid':
                print(f"Your ticket has already been paid. Thank you and have a nice day!")
            if self.ticketstatus[spacenum] == 'unpaid':
                payment = input("Please enter 'Pay' to submit payment. ")
                if payment.lower() == 'pay':
                    self.usedspaces.remove(spacenum)
                    self.tickets += 1
                    self.parkingspaces.append(spacenum)
                    self.ticketstatus[spacenum] = 'paid'
                    print(f"Thank you for your payment and have a nice day!")
                else:
                    print(f"Error, please try again.")
        else:
            print(f"Error, please try again.")
            
tesla = ParkingGarage(10, ['1','2','3','4','5','6','7','8','9','10'], [], {})

def run():
    print("Welcome to the parking garage!")

    while True:     
        answer = input("Would you like to park, pay, or leave? ")

        if answer.lower() == "park":
            clear_output()
            tesla.takeTicket()
        elif answer.lower() == "pay":
            clear_output()
            tesla.payForParking()
        elif answer.lower() == "leave":
            clear_output()
            tesla.leaveGarage()
        else: 
            print ("Error please try again!")
            
run()

