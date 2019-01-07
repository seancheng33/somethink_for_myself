import math
import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Drawing Arcs')

while True:

    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            sys.exit(0)

    screen.fill((0, 0, 200))
    color = 255, 0, 255
    position = 250, 150, 300, 300
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    width = 8

    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
    pygame.display.update()
