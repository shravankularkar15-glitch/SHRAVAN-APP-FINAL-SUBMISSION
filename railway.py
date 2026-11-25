
# DEVELOP A PYTHON APPICATION TO MAINTAIN  RAILWAY PASENGER BOOKING DETAILS 
class Passenger:
    def __init__(self, name, train_no, fare, category):
        self.name = name
        self.train_no = train_no
        self.fare = fare
        self.category = category

    def display(self):
        print("Passenger Name:", self.name)
        print("Train Number:", self.train_no)
        print("Ticket Fare:", self.fare)
        print("Category:", self.category)



class Railway:
    def __init__(self):
        self.passengers = []

    def add_booking(self):
        name = input("Enter Passenger Name: ")
        train = input("Enter Train Number: ")
        fare = float(input("Enter Ticket Fare: "))

        print("1. First Class")
        print("2. Second Class")
        print("3. Sleeper Class")

        choice = input("Enter Category: ")

        if choice == "1":
            category = "First Class"
        elif choice == "2":
            category = "Second Class"
        elif choice == "3":
            category = "Sleeper Class"
        else:
            print("Invalid Category")
            return

        p = Passenger(name, train, fare, category)
        self.passengers.append(p)
        print("Booking Added Successfully!")

    def display_bookings(self):
        for p in self.passengers:
            p.display()



r = Railway()

while True:
    print("1. Add Booking")
    print("2. Display Bookings")
    print("3. Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        r.add_booking()
    elif ch == "2":
        r.display_bookings()
    elif ch == "3":
        break
    else:
        print("Invalid Choice")
