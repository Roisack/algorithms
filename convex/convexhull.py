import os
import sys
import pygame
import math

class Point:
    x = 0
    y = 0
    color = pygame.Color(255,255,255,255)
    radius = 5
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

class Edge:
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    color = pygame.Color(0,255,0,255)

    def __init__(self, x0, y0, x1, y1):
        self.start_x = x0
        self.start_y = y0
        self.end_x = x1
        self.end_y = y1

    def draw(self, surface):
        pygame.draw.line(surface, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y))

# simply draw a line from each point to each point
def simpleLines(points):
    out = []
    for p in points:
        for o in points:
            if (o == p):
                continue
            out.append(Edge(p.x, p.y, o.x, o.y))

    return out

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((512,512))

    heightfield = pygame.Surface((512,512))
    heightfield.fill(pygame.Color(100,100,100,255))
    heightrect = heightfield.get_rect()

    points = []
    points.append(Point(100,200))
    points.append(Point(250,230))
    points.append(Point(300,300))
    points.append(Point(259,300))
    points.append(Point(260,210))
    points.append(Point(300,280))

    edges = simpleLines(points)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(pygame.Color(0,0,255,255))
        screen.blit(heightfield, heightrect)

        for p in points:
            p.draw(screen)

        for e in edges:
            e.draw(screen)

        pygame.display.flip()
