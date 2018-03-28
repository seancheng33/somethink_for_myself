'''
根据usingpython.com的教程而练习的内容
'''
import random, pygame, sys
from pygame.locals import *

# 定义一些常用的颜色
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# 定义云的起始位置
cloudx = -200
cloudy = 0

# 定义几个环境物件
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
CLOUD = 4

# 各元素的图片载入
textures = {
    DIRT: pygame.image.load('dirt.jpg'),
    GRASS: pygame.image.load('grass.jpg'),
    WATER: pygame.image.load('water.jpg'),
    COAL: pygame.image.load('coal.jpg'),
    CLOUD: pygame.image.load('cloud.png')
}

# 采集元素的统计
inventory = {
    DIRT: 0,
    GRASS: 0,
    WATER: 0,
    COAL: 0
}

# 元素个的大小和画面的元素行和列
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

# 元素资源词典，后面生成地形可以取值，没用到？
resources = [DIRT, GRASS, WATER, COAL]

# 生成地图
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0, 15)

        if randomNumber == 0:
            tile = COAL
        elif randomNumber == 1 or randomNumber == 2:
            tile = WATER
        elif randomNumber >= 3 and randomNumber <= 7:
            tile = GRASS
        else:
            tile = DIRT

        tilemap[rw][cl] = tile

pygame.init()

DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 50))
pygame.display.set_caption('MineCraft--2D by Python')
pygame.display.set_icon(pygame.image.load('icon.png'))

PLAYER = pygame.image.load('hero.png').convert_alpha()
playerPos = [0, 0]

INVFONT = pygame.font.Font(None, 18)

fpsClock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        # 按键事件，or 后面的按键没反应，原因未知，待排查
        elif event.type == KEYDOWN:
            if (event.key == K_RIGHT or event.type == K_d) and playerPos[0] < MAPWIDTH - 1:
                playerPos[0] += 1
            if (event.key == K_LEFT or event.type == K_a) and playerPos[0] > 0:
                playerPos[0] -= 1
            if (event.key == K_UP or event.type == K_w) and playerPos[1] > 0:
                playerPos[1] -= 1
            if (event.key == K_DOWN or event.type == K_s) and playerPos[1] < MAPHEIGHT - 1:
                playerPos[1] += 1
            if event.key == K_SPACE:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                inventory[currentTile] += 1
                tilemap[playerPos[1]][playerPos[0]] = DIRT

            if event.key == K_1:
                currentTile = tilemap[playerPos[1]][playerPos[0]]

                if inventory[DIRT] > 0:
                    inventory[DIRT] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = DIRT
                    inventory[currentTile] += 1
            if event.key == K_2:
                currentTile = tilemap[playerPos[1]][playerPos[0]]

                if inventory[GRASS] > 0:
                    inventory[GRASS] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = GRASS
                    inventory[currentTile] += 1

            if event.key == K_3:
                currentTile = tilemap[playerPos[1]][playerPos[0]]

                if inventory[WATER] > 0:
                    inventory[WATER] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = WATER
                    inventory[currentTile] += 1

            if event.key == K_4:
                currentTile = tilemap[playerPos[1]][playerPos[0]]

                if inventory[COAL] > 0:
                    inventory[COAL] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = COAL
                    inventory[currentTile] += 1

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURFACE.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))

    DISPLAYSURFACE.blit(PLAYER, (playerPos[0] * TILESIZE, playerPos[1] * TILESIZE))

    DISPLAYSURFACE.blit(textures[CLOUD].convert_alpha(), (cloudx, cloudy))
    cloudx += 1
    if cloudx > MAPWIDTH * TILESIZE:
        cloudy = random.randint(0, MAPHEIGHT * TILESIZE)
        cloudx = -200

    placePosition = 10
    for item in resources:
        DISPLAYSURFACE.blit(textures[item], (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 30
        textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
        DISPLAYSURFACE.blit(textObj, (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 50

    pygame.display.update()
    fpsClock.tick(24)
