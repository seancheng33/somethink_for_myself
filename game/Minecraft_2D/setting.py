import random, pygame


class Setting:
    def __init__(self):
        self.TILE_SIZE = 32
        self.MAP_WIDTH = 35
        self.MAP_HEIGHT = 20

        self.DIRT = pygame.image.load('img/dirt.png')  # 泥土
        self.GRASS = pygame.image.load('img/grass.png')  # 草地
        self.COAL = pygame.image.load('img/coal.png')  # 木材
        self.SAND = pygame.image.load('img/sand.png')  # 沙
        self.STONE = pygame.image.load('img/stone.png')  # 石头
        self.WATER = pygame.image.load('img/water.png')  # 水
        self.LAVA = pygame.image.load('img/lava.png')  # 熔岩

        # 先将地图全部生成为泥土
        self.tile_map = [[self.DIRT for w in range(self.MAP_WIDTH)] for h in range(self.MAP_HEIGHT)]
        # 生成随机的资源类型地图
        for rw in range(self.MAP_HEIGHT):
            for cl in range(self.MAP_WIDTH):
                num = random.randint(0, 30)
                if (num == 0) or (num == 1):
                    tile = self.COAL
                elif (num >= 2) and (num <= 4):
                    tile = self.GRASS
                elif (num >= 10) and (num <= 15):
                    tile = self.STONE
                elif num == 16:
                    tile = self.LAVA
                elif (num >= 17) and (num <= 22):
                    tile = self.WATER
                elif (num >= 23) and (num <= 24):
                    tile = self.SAND
                else:
                    tile = self.DIRT

                self.tile_map[rw][cl] = tile

        self.ROLE = pygame.image.load('img/role.png')  # 人物图片
        self.role_position = [0, 0]
        # 仓库资源的dict
        self.inventory = {self.DIRT: 0, self.GRASS: 0, self.COAL: 0, self.SAND: 0, self.STONE: 0, self.WATER: 0,
                          self.LAVA: 0}
        # 资源列表
        self.resources = [self.DIRT, self.GRASS, self.COAL, self.SAND, self.STONE, self.WATER, self.LAVA]

    # 画出地图,供主程序调用
    def draw_map(self, surface):
        for rw in range(self.MAP_HEIGHT):
            for cl in range(self.MAP_WIDTH):
                surface.blit(self.tile_map[rw][cl], (cl * self.TILE_SIZE, rw * self.TILE_SIZE))

    def draw_role(self, surface):
        surface.blit(self.ROLE, (self.role_position[0] * self.TILE_SIZE, self.role_position[1] * self.TILE_SIZE))
