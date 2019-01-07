import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Drawing Lines')

while True:

    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            sys.exit(0)

    screen.fill((0, 80, 0))
    color = 100, 255, 200
    width = 8

    pygame.draw.line(screen, color, (100, 100), (700, 500), width)
    pygame.display.update()
