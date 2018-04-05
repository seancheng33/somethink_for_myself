'''
根据网上的教程的练习作品，素材也是搜集自网络，再自行加工而成。
本联系作品的很多地方，可以用于RPG的雏形。
'''

import pygame, sys

from setting import Setting

pygame.init()
setting = Setting()

SURFACE = pygame.display.set_mode((setting.MAP_WIDTH * setting.TILE_SIZE, setting.MAP_HEIGHT * setting.TILE_SIZE + 80))
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
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and setting.role_position[1] > 0:
                setting.role_position[1] -= 1
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and setting.role_position[
                1] < setting.MAP_HEIGHT - 1:
                setting.role_position[1] += 1
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and setting.role_position[0] > 0:
                setting.role_position[0] -= 1
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and setting.role_position[
                0] < setting.MAP_WIDTH - 1:
                setting.role_position[0] += 1
            # 按空格键采集资源
            if event.key == pygame.K_SPACE:
                current_tile = setting.tile_map[setting.role_position[1]][setting.role_position[0]]
                setting.inventory[current_tile] += 1
                setting.tile_map[setting.role_position[1]][setting.role_position[0]] = setting.DIRT
            # 数字按键对应不同的资源，按对应的键，为将人物现有的资源摆放到地图上，同时地图上原来该资源存入人物的仓库
            if event.key == pygame.K_1:
                current_tile = setting.tile_map[setting.role_position[1]][setting.role_position[0]]
                if setting.inventory[setting.DIRT] > 0:
                    setting.inventory[setting.DIRT] -= 1
                    setting.tile_map[setting.role_position[1]][setting.role_position[0]] = setting.DIRT
                    setting.inventory[current_tile] += 1
            if event.key == pygame.K_2:
                current_tile = setting.tile_map[setting.role_position[1]][setting.role_position[0]]
                if setting.inventory[setting.GRASS] > 0:
                    setting.inventory[setting.GRASS] -= 1
                    setting.tile_map[setting.role_position[1]][setting.role_position[0]] = setting.GRASS
                    setting.inventory[current_tile] += 1
            if event.key == pygame.K_3:
                current_tile = setting.tile_map[setting.role_position[1]][setting.role_position[0]]
                if setting.inventory[setting.COAL] > 0:
                    setting.inventory[setting.COAL] -= 1
                    setting.tile_map[setting.role_position[1]][setting.role_position[0]] = setting.COAL
                    setting.inventory[current_tile] += 1
            if event.key == pygame.K_4:
                current_tile = setting.tile_map[setting.role_position[1]][setting.role_position[0]]
                if setting.inventory[setting.SAND] > 0:
                    setting.inventory[setting.SAND] -= 1
                    setting.tile_map[setting.role_position[1]][setting.role_position[0]] = setting.SAND
                    setting.inventory[current_tile] += 1
            if event.key == pygame.K_5:
                current_tile = setting.tile_map[setting.role_position[1]][setting.role_position[0]]
                if setting.inventory[setting.STONE] > 0:
                    setting.inventory[setting.STONE] -= 1
                    setting.tile_map[setting.role_position[1]][setting.role_position[0]] = setting.STONE
                    setting.inventory[current_tile] += 1
            if event.key == pygame.K_6:
                current_tile = setting.tile_map[setting.role_position[1]][setting.role_position[0]]
                if setting.inventory[setting.WATER] > 0:
                    setting.inventory[setting.WATER] -= 1
                    setting.tile_map[setting.role_position[1]][setting.role_position[0]] = setting.WATER
                    setting.inventory[current_tile] += 1
            if event.key == pygame.K_7:
                current_tile = setting.tile_map[setting.role_position[1]][setting.role_position[0]]
                if setting.inventory[setting.LAVA] > 0:
                    setting.inventory[setting.LAVA] -= 1
                    setting.tile_map[setting.role_position[1]][setting.role_position[0]] = setting.LAVA
                    setting.inventory[current_tile] += 1
    # 画出地图
    setting.draw_map(SURFACE)
    # 画人物
    setting.draw_role(SURFACE)

    # 以下为画出仓库资源
    placePosition = 50

    for item in setting.resources:
        SURFACE.blit(item, (placePosition, setting.MAP_HEIGHT * setting.TILE_SIZE + 24))
        placePosition += 50
        textObj = pygame.font.Font(None, 32).render(str(setting.inventory[item]), True, (255, 255, 255), (0, 0, 0))
        SURFACE.blit(textObj, (placePosition, setting.MAP_HEIGHT * setting.TILE_SIZE + 30))
        placePosition += 50

    pygame.display.update()
