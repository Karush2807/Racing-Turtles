import turtle #for 2d graphics
import time #for time delay
WIDTH, HEIGHT = 500, 500



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

def init_rabits():
    screen= turtle.Screen()#will initialise a screen for us
    screen.setup(WIDTH, HEIGHT)#size of the screen
    screen.title("Racing Rabits")#title of the screen

racers=num_of_rabits()
init_rabits()

racer=turtle.Turtle()#will create a turtle object
racer.forward(100)#will move the turtle forward by 100 units    \
racer.left(90)
racer.forward(90)
racer.right(100)
time.sleep(10)