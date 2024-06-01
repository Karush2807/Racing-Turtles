import turtle #for 2d graphics
import time #for time delay
import random #for random number generation
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']




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

def create_turtles(colors):
	turtles = []
	spacingx = WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles

def init_rabits():
    screen= turtle.Screen()#will initialise a screen for us
    screen.setup(WIDTH, HEIGHT)#size of the screen
    screen.title("Racing Rabits")#title of the screen

racers=num_of_rabits()
init_rabits()


random.shuffle(COLORS)
colors=COLORS[:racers]
print(colors)



turtle.done()#will keep the screen open4