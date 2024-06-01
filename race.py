import turtle # for 2D graphics
import time # for time delay
import random # for random number generation

# Screen dimensions and available colors for turtles
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan'] #colors decided for the turtles

# Function to get the number of racers from user input
def num_of_rabits():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Numeric input allowed only!")
            continue # Start the while loop again for invalid input

        if racers not in range(2, 11):
            print("Invalid input! Enter again")
        else:
            return racers

# Function to handle the race logic
def race(colors):
    turtles = create_turtles(colors) # Create turtle objects

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20) # Random distance for each move
            racer.forward(distance) # Move the turtle forward

            x, y = racer.pos() # Get the current position of the turtle
            if y >= HEIGHT // 2 - 20: # Check if the turtle reached the finish line
                return colors[turtles.index(racer)] # Return the color of the winning turtle

# Function to create turtles with given colors
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1) # Calculate spacing for turtle placement
    for i, color in enumerate(colors):
        racer = turtle.Turtle() # Create turtle object
        racer.color(color)
        racer.shape('turtle')
        racer.left(90) # Point the turtle upwards
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20) # Set initial position
        racer.pendown()
        turtles.append(racer) # Add turtle to the list

    return turtles

# Function to initialize the turtle graphics screen
def init_rabits():
    screen = turtle.Screen() # Initialize screen
    screen.setup(WIDTH, HEIGHT) # Set screen size
    screen.title("Racing Rabbits") # Set screen title

# Main logic
racers = num_of_rabits() # Get number of racers
init_rabits() # Initialize screen

random.shuffle(COLORS) # Shuffle the colors
colors = COLORS[:racers] # Select colors for the number of racers
print(colors)

winner = race(colors) # Start the race
turtle.done() # Keep the screen open
print(winner) # Print the winning turtle color
