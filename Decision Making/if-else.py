age = int(input("Enter your age: "))
studentId = input("do you have student ID (yes/no)?").lower()
movieTime = int(input("What the time? (24hrs format)"))

if age >= 18:
    print("Can book the Ticket")
elif age < 18:
    if studentId == "yes" and movieTime < 1800:
        print("you can book the Ticket")
    else:
        print("Time is up for kids")
else:
    print("You are not allowed to book the Ticket")


