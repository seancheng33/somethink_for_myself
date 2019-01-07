import sys
import pygame
from pygame.locals import *

pygame.init()
white = 255, 255, 255
blue = 0, 0, 126
screen = pygame.display.set_mode((1024, 768))
myfont = pygame.font.Font(None, 60)
textImage = myfont.render("Pygame study demo 01.", True, white)

while True:

    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit
            sys.exit(0)

    screen.fill(blue)
    screen.blit(textImage, (100, 100))

    pygame.display.update()
