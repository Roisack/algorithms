import os
import sys
import pygame
import random

size_x = 512
size_y = 512

def randomColor():

    c = random.randrange(0,255)

    out = pygame.Color(c,c,c,255)
    return out

def getHeightfield():
    heightfield = pygame.Surface((size_x, size_y))
    x = 0
    y = 0
    for x in range(0, size_x):
        for y in range(0, size_y):
            c = randomColor()
            heightfield.set_at((x,y), c)
    return heightfield

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((512,512))

    heightfield = getHeightfield()
    heightrect = heightfield.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(pygame.Color(0,0,255,255))
        screen.blit(heightfield, heightrect)
        pygame.display.flip()
