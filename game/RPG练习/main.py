'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/6/14 
@Program  : 练习rpg的游戏，这个是主入口文件。
'''
import pygame
from pygame.locals import *
import mapdata
from GlobalSetting import GlobalSetting
from sysfunction import close_program


def startscreen():
    title = setting.INVFONT.render('中文的标题', True, (255, 255, 255), setting.BGCOLOR)
    titleRect = title.get_rect()
    titleRect.top = 100
    titleRect.centerx = int(setting.SCREENWIDTH / 2)

    setting.SCREENFACE.blit(title, titleRect)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                close_program()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    close_program()
                return

        pygame.display.update()
        setting.FPSCLOCK.tick()


def draw_map(mapObj, gameStateObj):
    mapWidth = len(mapObj[0]) * setting.TILESIZE
    mapHeight = len(mapObj) * setting.TILESIZE
    mapSurface = pygame.Surface((mapWidth, mapHeight))

    rolex, roley = gameStateObj['player']

    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            mapSurface.blit(setting.TILEMAPPING[mapObj[x][y]], (y * setting.TILESIZE, x * setting.TILESIZE))

    role = pygame.image.load('img/horngirl.png')
    role_rect = pygame.Rect(rolex * setting.TILESIZE, roley * setting.TILESIZE, setting.TILESIZE, setting.TILESIZE)

    mapSurface.blit(role, role_rect)

    return mapSurface


def show_menu():
    while True:
        pygame.draw.rect(setting.SCREENFACE, (0, 255, 0), (150, 450, 100, 50))
        pygame.display.update()
        setting.FPSCLOCK.tick()


def redraw_map(mapObj, gameStateObj):
    x, y = gameStateObj['player']
    mapwidth = mapObj.get_width() / setting.TILESIZE
    mapheight = mapObj.get_height() / setting.TILESIZE

    half_x = mapwidth / 2
    half_y = mapheight / 2

    if (x - half_x) > 0:
        if x > (mapwidth - setting.TILEWIDTH):
            offsetX = (mapwidth - setting.TILEWIDTH - 1) * setting.TILESIZE
        else:
            offsetX = (x - half_x) * setting.TILESIZE
    else:
        offsetX = 0 * setting.TILESIZE

    if (y - half_y) > 0:
        if y > (mapheight - setting.TILEHEIGHT):
            offsetY = (mapheight - setting.TILEHEIGHT - 1) * setting.TILESIZE
        else:
            offsetY = (y - half_y) * setting.TILESIZE
    else:
        offsetY = 0 * setting.TILESIZE

    if mapwidth > setting.TILEWIDTH and mapheight > setting.TILEHEIGHT:
        sub_map = Rect(offsetX, offsetY, setting.SCREENWIDTH, setting.SCREENHEIGHT)
        mapSurface = mapObj.subsurface(sub_map)
        return mapSurface

    return mapObj


def run_map(mapList, gameStateObj):
    global currentMapName

    currentMapName = gameStateObj['map name']

    mapObj = mapList[currentMapName]

    menu = False

    while True:
        setting.SCREENFACE.fill(setting.BGCOLOR)

        map = draw_map(mapObj, gameStateObj)
        mapRect = map.get_rect()
        mapRect.left = 0
        mapRect.top = 0
        map = redraw_map(map, gameStateObj)

        setting.SCREENFACE.blit(map, mapRect)
        x, y = gameStateObj['player']

        for event in pygame.event.get():
            if event.type == QUIT:
                close_program()
            elif event.type == KEYDOWN:
                # 控制角色的移动
                if event.key == K_LEFT:
                    if x > 0:
                        gameStateObj['player'] = (x - 1, y)
                elif event.key == K_RIGHT:
                    if x < setting.TILEWIDTH:
                        gameStateObj['player'] = (x + 1, y)
                elif event.key == K_UP:
                    if y > 0:
                        gameStateObj['player'] = (x, y - 1)
                elif event.key == K_DOWN:
                    if y < setting.TILEHEIGHT:
                        gameStateObj['player'] = (x, y + 1)

                elif event.key == K_m:
                    if not menu:
                        pygame.draw.rect(setting.SCREENFACE, (0, 125, 0), (150, 450, 100, 50))
                        menu = True
                        return  # 这个return可以让地图静止
                    else:
                        menu = True

        for item in mapdata.inter_postion[currentMapName].items():
            # print(item[0],item[1])
            if (x, y) == item[1]:
                currentMapName = item[0][2:]
                gameStateObj['map name'] = currentMapName
                gameStateObj['player'] = mapdata.role_postion[currentMapName]
                mapObj = mapList[currentMapName]

        pygame.display.update()
        setting.FPSCLOCK.tick()


def main():
    global setting
    setting = GlobalSetting()

    mapList = {'base': mapdata.mapBase, 'sea': mapdata.mapSea}

    gameStateObj = {
        'player': mapdata.role_postion['base'],
        'map name': 'base',

    }

    setting.SCREENFACE.fill(setting.BGCOLOR)
    # startscreen()
    run_map(mapList, gameStateObj)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                close_program()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    close_program()

        pygame.display.update()
        setting.FPSCLOCK.tick()


if __name__ == '__main__':
    main()
