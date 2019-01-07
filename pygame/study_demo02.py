import sys
import pygame
from pygame.locals import *

pygame.init()
white = 255, 255, 255
blue = 0, 0, 126
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Drawing Circles')

while True:

    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            sys.exit(0)

    screen.fill((0, 0, 200))
    color = 255, 255, 0
    postion = 400, 300
    radius = 250
    width = 10
    pygame.draw.circle(screen, color, postion, radius, width)

    pygame.display.update()
