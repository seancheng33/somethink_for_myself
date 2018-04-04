'''
根据网上的教程的练习作品，素材也是搜集自网络，再自行加工而成。
本联系作品的很多地方，可以用于RPG的雏形。
'''

import pygame, sys, random
from pygame.locals import *

pygame.init()

TILE_SIZE = 32
MAP_WIDTH = 35
MAP_HEIGHT = 20

DIRT = pygame.image.load('img/dirt.png')    # 泥土
GRASS = pygame.image.load('img/grass.png')  # 草地
COAL = pygame.image.load('img/coal.png')    # 木材
SAND = pygame.image.load('img/sand.png')    # 沙
STONE = pygame.image.load('img/stone.png')  # 石头
WATER = pygame.image.load('img/water.png')  # 水
LAVA = pygame.image.load('img/lava.png')  # 熔岩
# 先将地图全部生成为泥土
tile_map = [[DIRT for w in range(MAP_WIDTH)] for h in range(MAP_HEIGHT)]
# 生成随机的资源类型地图
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
        elif (num >= 23) and (num <= 24):
            tile = SAND
        else:
            tile = DIRT

        tile_map[rw][cl] = tile

ROLE = pygame.image.load('img/role.png')    # 人物图片
role_position = [0, 0]
# 仓库资源的dict
inventory = {DIRT: 0, GRASS: 0, COAL: 0, SAND: 0, STONE: 0, WATER: 0, LAVA: 0}
# 资源列表
resources = [DIRT, GRASS, COAL, SAND, STONE, WATER, LAVA]

SURFACE = pygame.display.set_mode((MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE + 80))
pygame.display.set_caption('MINECRAFT 2D')

while True:
    # 按键事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)
            # 人物移动控制，可以是方向键，也可以是wasd
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and role_position[1] > 0:
                role_position[1] -= 1
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and role_position[1] < MAP_HEIGHT - 1:
                role_position[1] += 1
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and role_position[0] > 0:
                role_position[0] -= 1
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and role_position[0] < MAP_WIDTH - 1:
                role_position[0] += 1
            # 按空格键采集资源
            if event.key == pygame.K_SPACE:
                current_tile = tile_map[role_position[1]][role_position[0]]
                inventory[current_tile] += 1
                tile_map[role_position[1]][role_position[0]] = DIRT
            # 数字按键对应不同的资源，按对应的键，为将人物现有的资源摆放到地图上，同时地图上原来该资源存入人物的仓库
            if event.key == pygame.K_1:
                current_tile = tile_map[role_position[1]][role_position[0]]
                if inventory[DIRT] > 0:
                    inventory[DIRT] -= 1
                    tile_map[role_position[1]][role_position[0]] = DIRT
                    inventory[current_tile] += 1
            if event.key == pygame.K_2:
                current_tile = tile_map[role_position[1]][role_position[0]]
                if inventory[GRASS] > 0:
                    inventory[GRASS] -= 1
                    tile_map[role_position[1]][role_position[0]] = GRASS
                    inventory[current_tile] += 1
            if event.key == pygame.K_3:
                current_tile = tile_map[role_position[1]][role_position[0]]
                if inventory[COAL] > 0:
                    inventory[COAL] -= 1
                    tile_map[role_position[1]][role_position[0]] = COAL
                    inventory[current_tile] += 1
            if event.key == pygame.K_4:
                current_tile = tile_map[role_position[1]][role_position[0]]
                if inventory[SAND] > 0:
                    inventory[SAND] -= 1
                    tile_map[role_position[1]][role_position[0]] = SAND
                    inventory[current_tile] += 1
            if event.key == pygame.K_5:
                current_tile = tile_map[role_position[1]][role_position[0]]
                if inventory[STONE] > 0:
                    inventory[STONE] -= 1
                    tile_map[role_position[1]][role_position[0]] = STONE
                    inventory[current_tile] += 1
            if event.key == pygame.K_6:
                current_tile = tile_map[role_position[1]][role_position[0]]
                if inventory[WATER] > 0:
                    inventory[WATER] -= 1
                    tile_map[role_position[1]][role_position[0]] = WATER
                    inventory[current_tile] += 1
            if event.key == pygame.K_7:
                current_tile = tile_map[role_position[1]][role_position[0]]
                if inventory[LAVA] > 0:
                    inventory[LAVA] -= 1
                    tile_map[role_position[1]][role_position[0]] = LAVA
                    inventory[current_tile] += 1
    # 画出地图
    for rw in range(MAP_HEIGHT):
        for cl in range(MAP_WIDTH):
            SURFACE.blit(tile_map[rw][cl], (cl * TILE_SIZE, rw * TILE_SIZE))
    # 画人物
    SURFACE.blit(ROLE, (role_position[0] * TILE_SIZE, role_position[1] * TILE_SIZE))

    # 以下为画出仓库资源
    placePosition = 50

    for item in resources:
        SURFACE.blit(item, (placePosition, MAP_HEIGHT * TILE_SIZE + 24))
        placePosition += 50
        textObj = pygame.font.Font(None, 32).render(str(inventory[item]), True, (255, 255, 255), (0, 0, 0))
        SURFACE.blit(textObj, (placePosition, MAP_HEIGHT * TILE_SIZE + 30))
        placePosition += 50

    pygame.display.update()
