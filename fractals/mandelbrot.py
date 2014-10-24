import os
import sys
import pygame
import random
import math

size_x = 512
size_y = 512

focus_point = [-1, 0.4]
#x_range = 0.15
#y_range = 0.15
x_range = 5.0
y_range = 5.0

max_iterations = 10

palette = []
num_of_colors = max_iterations

def randomColor():
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    return pygame.Color(r,g,b,255)

def generatePalette():
    for x in range(0, num_of_colors+1):
        palette.append(randomColor())
    
def lerp(x1, x2, a):
    return x1 * (1.0 - a) + a * x2;

def man_equation(z, c, n, old_z):
    if (len(c) != 2):
        print("error! len(c) is " +  str(len(c)))
        return 0
    
    if (n >= max_iterations):
        return max_iterations
    
    old_z = z
    z_squared = [ z[0]*z[0] - z[1]*z[1], 2*z[0]*z[1] ]
    new_z = [z_squared[0] + c[0], z_squared[1] + c[1]]
    
    # If this complex number keeps getting the same values over and over again
    if (old_z[0] == new_z[0] and old_z[1] == new_z[1]):
        return max_iterations
    
    # If this complex number has escaped this iteration
    if ( (new_z[0]*new_z[0]) + (new_z[1]*new_z[1]) > 4.0):
        return n
    
    n = n + 1
    
    return man_equation(new_z, c, n, old_z)

def man_color(c):
    iterations = man_equation([0.0, 0.0], c, 0, [0.0, 0.0])
    iter_color = palette[iterations]
    if (iterations >= max_iterations):
        iter_color = pygame.Color(255,255,255,255)
    return iter_color

def getTexture():
    man_set = pygame.Surface((size_x, size_y))
    color = pygame.Color(100,0,0,255)
    complex = [0,0]
    x = 0
    y = 0
    
    for x in range(0, size_x-1):
        for y in range(0, size_y-1):
            complex[0] = focus_point[0] + lerp(-x_range, x_range, x/float(size_x))
            complex[1] = focus_point[1] + lerp(y_range, -y_range, y/float(size_y))
            color = man_color(complex)
            man_set.set_at((x,y), color)
    return man_set

def printSet(texture):

    for x in range(0, size_x):
        sys.stdout.write(str(x) + "\t")
    sys.stdout.write("\n")
    
    for x in range(0, size_x):
        for y in range(0, size_y):
            sys.stdout.write(str(texture.get_at((x,y)).r) + "\t ")
        sys.stdout.write("\n")
    
if __name__ == "__main__":
    pygame.init()
    
    generatePalette()
    
    screen = pygame.display.set_mode((size_x,size_x))
    texture = getTexture()
    texture_rect = texture.get_rect()
    
    #printSet(texture)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(pygame.Color(0,0,255,255))
        screen.blit(texture, texture_rect)
        pygame.display.flip()