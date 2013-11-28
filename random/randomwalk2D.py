# Random walk in two dimensions

import turtle # turtles are cute
import random
import math

steps = 200
step_min_length = 1
step_max_length = 5
pi = 3.14159

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
        angle = random.uniform(0, 2*pi)
        # Get step length
        length = random.randrange(step_min_length, step_max_length)
        current_x += length * math.cos(angle)
        current_y += length * math.sin(angle)
        path.append((current_x, current_y))
    
    return path

# Returns a random direction for a random walk considering
# that the walk should be more biased towards the center of a circle
# TODO: Fix bugs with wrong directione being calculated
def circular_gradient_direction(position_x, position_y):
    circle_radius = 50.0
    distance_to_center = math.sqrt((position_x * position_x) + (position_y * position_y))
    
    # If at non-zero position
    if (position_x != 0 and position_y != 0):
        direction_towards_center = 0
        if (position_x >= 0 and position_y >= 0):
            direction_towards_center = pi + math.atan(position_x / position_y)
        elif (position_x >= 0 and position_y < 0):
            direction_towards_center = pi/2.0 - math.atan(position_x / position_y)
        elif (position_x < 0 and position_y < 0):
            direction_towards_center = math.atan(position_x / position_y)
        elif (position_x < 0 and position_y > 0):
            direction_towards_center = math.atan(position_x / position_y)
        direction_towards_center_deg = direction_towards_center * (180.0 / pi)
        print(direction_towards_center_deg, position_x, position_y)
    else:
        # Use random value for the odd chance that the division is at zero
        # also kicks off the first step
        return random.uniform(0, 2*pi)
    
    # How far from the center are we in terms of percentage?
    distance_coefficient = distance_to_center / circle_radius
    
    # Final angle is the distance towards center + random value that is biased more for longer distances
    random_angle = random.uniform(0, 2*pi)
    return direction_towards_center + (random_angle * (1.0 / distance_coefficient))

def random_walk_circular_gradient(steps):
    path = []
    current_x = 0
    current_y = 0
    
    for s in range(0, steps):
        # Get random angle for current position
        angle = circular_gradient_direction(current_x, current_y)
        
        # Step 2 units in the direction given by the gradient angle function
        current_x += 5 * math.cos(angle)
        current_y += 5 * math.sin(angle)
        
        path.append((current_x, current_y))
        
    return path

if __name__ == "__main__":
    #turtle.speed('fastest')
    turtle.speed('fastest')
    
    #path = random_walk_right_angles(steps)
    #path = random_walk_2D(steps)
    path = random_walk_circular_gradient(steps)
    
    for x, y in path:
        turtle.goto(x*10, y*10)
        
    turtle.exitonclick()
    