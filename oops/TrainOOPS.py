class IndianRailwayTrains():

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def fareInfo(self):
        print(f"The price of the ticket is: {self.fare}")

    def bookTickets(self):
        if(self.seats>0):
            print(f"Your ticket has booked and your ticket number is IRTNO00_{self.seats}")
            self.seats= self.seats-1
        else:
            print("Sorry no tickets available, pleae try in tatkal")     

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The fare of the train is {self.fare}")
        print(f"The seating capacity of the train is now {self.seats}")      

    def cancelTicket(self, seatNo):
        pass

func_EnterName= input("Please Enter Train Name: ")

intercity = IndianRailwayTrains(func_EnterName, 90, 2)
duronto = IndianRailwayTrains(func_EnterName, 78, 234)
rajdhani = IndianRailwayTrains(func_EnterName, 122, 150)

if func_EnterName=="intercity express":
    intercity.bookTickets()
    intercity.bookTickets()
    intercity.bookTickets()
    intercity.getStatus()
    
elif func_EnterName=="duronto express":
    duronto.bookTickets()
    duronto.getStatus()
    
elif func_EnterName=="rajdhani express":
    rajdhani.bookTickets()
    rajdhani.getStatus()
    
else:
    print("train name is incorrect")    



  
