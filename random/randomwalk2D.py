# Random walk in two dimensions

import turtle # turtles are cute
import random
import math

steps = 200
step_min_length = 1
step_max_length = 5

# Produces a list containing (x,y) tuples
# steps: The number of steps that are calculated
# Steps are only taken in 90 degree angles
def random_walk_right_angles(steps):
    path = []
    current_x = 0
    current_y = 0
    
    # Do the walk
    for s in range (0, steps):
    
        # Get step direction
        direction = random.randint(1, 4)
        # Get some random length
        length = random.randrange(step_min_length, step_max_length)
        if (direction == 1):
            current_x += length
        elif (direction == 2):
            current_y += length
        elif (direction == 3):
            current_x -= length
        elif (direction == 4):
            current_y -= length
        else:
            print("error")
        path.append((current_x, current_y))
    
    return path

# Random walk in two dimensions without limiting the walk to 90 degree turns
def random_walk_2D(steps):
    path = []
    current_x = 0
    current_y = 0
    
    for s in range(0, steps):
        # Get step direction, a random angle
        angle = random.randrange(0, 360)
        # Get step length
        length = random.randrange(step_min_length, step_max_length)
        current_x += length * math.cos(angle)
        current_y += length * math.sin(angle)
        path.append((current_x, current_y))
    
    return path

if __name__ == "__main__":
    turtle.speed('fastest')
    
    path = random_walk_2D(steps)
    
    for x, y in path:
        turtle.goto(x*10, y*10)
        
    turtle.exitonclick()
    