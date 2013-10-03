import os
import sys
import pygame
import random

size_x = 256
size_y = 256
max_height = 255
line_count = 15
fault_change = 15

# Returns a pygame.Color with all channels set to c
def getBWColor(c):
    return pygame.Color(c,c,c,255)

def getHeightfield():
    heightfield = pygame.Surface((size_x, size_y))
    # Init to flat terrain
    heightfield.fill(getBWColor(max_height/2))
    for i in range(1, line_count):
        x0 = random.randrange(0, heightfield.get_width() - fault_change)
        y0 = random.randrange(0, heightfield.get_height() - fault_change)
        x1 = random.randrange(0, heightfield.get_width() - fault_change)
        y1 = random.randrange(0, heightfield.get_height() - fault_change)

        for x in range(0, heightfield.get_width() - fault_change):
            for y in range(0, heightfield.get_height() - fault_change):
                if ((x1 - x0) * (y - y0) - (y1 - y0) * (x - x0) > 0):
                    temp1 = heightfield.get_at((x, y + fault_change))
                    temp2 = getBWColor(max_height)
                    smaller = min(temp1, temp2)
                    heightfield.set_at((x,y), smaller)
                else:
                    temp1 = heightfield.get_at((x, y + fault_change))
                    temp2 = getBWColor(max_height)
                    larger = max(temp1, 0)
                    heightfield.set_at((x,y), larger)
                    heightfield.set_at((x,y), getBWColor(max_height))
        print("Iterations done: " + str(i))
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
