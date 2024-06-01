# Racing Rabbits

## Overview
Racing Rabbits is a simple graphical game created using Python's `turtle` module. The game allows users to input the number of rabbit racers (turtles) and then visualizes a race where the rabbits move forward randomly until one reaches the finish line.

## Requirements
- Python 3.x
- `turtle` module (pre-installed with Python)

## How to Run
1. Clone or download the project.
2. Ensure you have Python installed.
3. Run the `race.py` script.

## Code Explanation

### Constants
- `WIDTH`, `HEIGHT`: Dimensions of the turtle graphics window.
- `COLORS`: List of colors to be assigned to the turtles.

### Functions

#### `num_of_rabits()`
Prompts the user to input the number of racers between 2 and 10. Ensures valid input and returns the number of racers as an integer.

```python
def num_of_rabits():
    racers=0
    while True: 
        racers=input("enter the number of racer (2-10) : ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print("numeric input allowed only!")
            continue
        if racers not in range(2,11):
            print("invalid input! enter again")
        else:
            return racers
```
#### `create_turtles(colors)`


Creates turtle objects for each racer, assigns them a color, and positions them at the starting line.

```python
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
```

#### `init_rabits()`

Initializes the turtle graphics screen with the specified width, height, and title.

```python
def init_rabits():
    screen= turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Racing Rabits")
```

#### `race(colors)`
Simulates' the race by moving each turtle forward by a random distance in each iteration. The race continues until one of the turtles crosses the finish line.

```python
def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 20:
                return colors[turtles.index(racer)]
```