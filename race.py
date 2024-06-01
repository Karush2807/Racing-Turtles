import turtle #for 2d graphics

def num_of_rabits():
    racers=0
    while True: 
        #jb tk user valid input nhi deta
        racers=input("enter the number of racer (2-10) : ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print("numeric input allowed only!")
            continue #will start the while loop again

        if racers not in range(2,11):
            print("invalid input! enter again")
    
        else:
            return f' the total number of rabits in the race are: {racers}'


racers=num_of_rabits()
print(racers)