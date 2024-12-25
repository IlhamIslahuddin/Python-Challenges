import turtle
import random

# Set up the screen and the turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=600,height=600)
pirate = turtle.Turtle() 
pirate.speed(5)  # Set the turtle to the fastest speed

border_left = -250
border_right = 250
border_top = 250
border_bottom = -250

# Function to simulate the random walk
def drunk_pirate(steps):
    for _ in range(steps):
        # Make a random turn (between 0 and 360 degrees)
        pirate.left(random.randint(0, 360))
        
        # Move 100 steps forward
        pirate.forward(100)
        current_x, current_y = pirate.position()

        # Calculate the new position

        # Check if the turtle is out of bounds and correct the position if necessary
        x, y = pirate.position()

        # Ensure the turtle stays within the boundaries
        if x < border_left:
            pirate.setx(border_left)
        elif x > border_right:
            pirate.setx(border_right)

        if y < border_bottom:
            pirate.sety(border_bottom)
        elif y > border_top:
            pirate.sety(border_top)

# Call the function to simulate the drunk pirate's path
drunk_pirate(20)  # Number of random steps the pirate will take
screen.mainloop()
