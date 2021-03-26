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
        confirm = input("Are you sure you would like to take a ticket? (Yes/No) ")
        if confirm.lower() == "yes":
            self.tickets -= 1
            print(self.parkingspaces)
            spaceselect = input("Please select a parking space from the previous list: ")
            if spaceselect in self.parkingspaces:
                self.parkingspaces.remove(spaceselect)
            if spaceselect not in self.usedspaces:
                self.usedspaces.append(spaceselect)
            self.ticketstatus[spaceselect] == unpaid
        elif confirm.lower() == "no":
            print(f"Have a nice day!")
        else:
            print(f"Please try again.")

    def payForParking(self):
        print(self.usedspaces)
        payforspace = input("From the previous list what parking spot are you paying for? ")
        if payforspace in self.usedspaces:
            payment = input("Please enter 'Pay' to submit payment. ")
            if payment.lower() == 'pay':
                self.usedspaces.remove(payforspace)
                self.tickets += 1
                self.parkingspaces.append(payforspace)
                self.ticketstatus[payforspace] == paid
                print(f"Thank you for your payment!")
        if payforspace not in self.usedspace:
            print(f"Error, please try again.")

    def leaveGarage(self):
        print(self.usedspaces)
        spacenum = input("What was your parking space number? ")
        if spacenum in self.ticketstatus:
            if ticketstatus.get(spacenum) == paid:
                print(f"Thank you and have a nice day!")
            if ticketstatus.get(spacenum) == unpaid:
                payment = input("Please enter 'Pay' to submit payment. ")
                if payment.lower() == 'pay':
                    self.usedspaces.remove(spacenum)
                    self.tickets += 1
                    self.parkingspaces.append(spacenum)
                    self.ticketstatus[spacenum] == paid
                    print(f"Thank you for your payment and have a nice day!")
                else:
                    print(f"Error, please try again.")
        else:
            print(f"Error, please try again.")

        
        
tesla = ParkingGarage(10, [1,2,3,4,5,6,7,8,9,10], [], {})

def run():
    print("welcome to the parking garage!")

    while True:     
        answer = input("would you like to park pay or leave? ")

        if response.lower()=="park":
            tesla.takeTicket()
        elif response.lower()=="pay":
            tesla.payForParking()
        elif response.lower()=="leave":
            tesla.leaveGarage()
        else: 
            print ("Error please try again!")

            


