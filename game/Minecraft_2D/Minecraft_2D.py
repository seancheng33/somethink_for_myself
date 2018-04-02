import random

import pygame, sys
from pygame.locals import *

pygame.init()

TILE_SIZE = 32
MAP_WIDTH = 35
MAP_HEIGHT = 20

DIRT = pygame.image.load('img/dirt.png')
GRASS = pygame.image.load('img/grass.png')
COAL = pygame.image.load('img/coal.png')
SAND = pygame.image.load('img/sand.png')
STONE = pygame.image.load('img/stone.png')
WATER = pygame.image.load('img/water.png')
LAVA = pygame.image.load('img/lava.png')

tile_map = [[DIRT for w in range(MAP_WIDTH)] for h in range(MAP_HEIGHT)]

for rw in range(MAP_HEIGHT):
    for cl in range(MAP_WIDTH):
        num = random.randint(0, 30)
        if (num == 0) or (num == 1):
            tile = COAL
        elif (num >= 2) and (num <= 4):
            tile = GRASS
        elif (num >= 10) and (num <= 15):
            tile = STONE
        elif num == 16:
            tile = LAVA
        elif (num >= 17) and (num <= 22):
            tile = WATER
        else:
            tile = DIRT

        tile_map[rw][cl] = tile

ROLE = pygame.image.load('img/role.png')
role_position = [0,0]

inventory = {DIRT: 0, GRASS: 0, COAL: 0, SAND: 0, STONE: 0, WATER: 0, LAVA: 0}

SURFACE = pygame.display.set_mode((MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))
pygame.display.set_caption('MINECRAFT 2D')

while True:
    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)

            if (event.key == pygame.K_UP or event.key == pygame.K_w) and role_position[1] > 0:
                role_position[1] -= 1
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and role_position[1] < MAP_HEIGHT - 1:
                role_position[1] += 1
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and role_position[0] > 0:
                role_position[0] -= 1
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and role_position[0] < MAP_WIDTH - 1:
                role_position[0] += 1

            if event.key == pygame.K_SPACE:
                current_tile = tile_map[role_position[1]][role_position[0]]
                inventory[current_tile] += 1
                tile_map[role_position[1]][role_position[0]] = DIRT
                # print(inventory)

    for rw in range(MAP_HEIGHT):
        for cl in range(MAP_WIDTH):
            SURFACE.blit(tile_map[rw][cl], (cl * TILE_SIZE, rw * TILE_SIZE))

    SURFACE.blit(ROLE,(role_position[0]*TILE_SIZE,role_position[1]*TILE_SIZE))

    pygame.display.update()
