'''
@Author      : sean cheng
@Email       : aya234@163.com
@CreateTime  : 2018/6/13
@progarm     : pygame练习，一个类似于仓库番的游戏
'''
import copy
import os
import random
import sys

import pygame
from pygame.locals import *

FPS = 30
WINWIDTH = 800
WINHEIGHT = 600
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 45

CAM_MOVE_SPEED = 5

OUTSIDE_DECORATION_PCT = 20

BRIGHTBLUE = (0, 170, 255)
WHITE = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage

    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

    pygame.display.set_caption('Star Pusher')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    IMAGESDICT = {'boy': pygame.image.load('img/boy.png'),
                  'catgirl': pygame.image.load('img/catgirl.png'),
                  'horngirl': pygame.image.load('img/horngirl.png'),
                  'pinkgorl': pygame.image.load('img/pinkgirl.png'),
                  'princess': pygame.image.load('img/princess.png'),
                  'inside floor': pygame.image.load('img/Plain_Block.png'),
                  'outside floor': pygame.image.load('img/Grass_Block.png'),
                  'uncovered goal': pygame.image.load('img/RedSelector.png'),
                  'covered goal': pygame.image.load('img/Selector.png'),
                  'rock': pygame.image.load('img/Rock.png'),
                  'star': pygame.image.load('img/Star.png'),
                  'solved': pygame.image.load('img/star_solved.png'),
                  'title': pygame.image.load('img/star_title.png'),
                  'short tree': pygame.image.load('img/Tree_Short.png'),
                  'tall tree': pygame.image.load('img/Tree_Tall.png'),
                  'ugly tree': pygame.image.load('img/Tree_Ugly.png'),
                  'corner': pygame.image.load('img/Wall_Block_Tall.png'),
                  'wall': pygame.image.load('img/Wood_Block_Tall.png'),
                  }

    TILEMAPPING = {'x': IMAGESDICT['corner'],
                   '#': IMAGESDICT['wall'],
                   'o': IMAGESDICT['inside floor'],
                   ' ': IMAGESDICT['outside floor']}

    OUTSIDEDECOMAPPING = {'1': IMAGESDICT['rock'],
                          '2': IMAGESDICT['short tree'],
                          '3': IMAGESDICT['tall tree'],
                          '4': IMAGESDICT['ugly tree']}

    currentImage = 0
    PLAYERIMAGES = [IMAGESDICT['princess'],
                    IMAGESDICT['boy'],
                    IMAGESDICT['catgirl'],
                    IMAGESDICT['horngirl'],
                    IMAGESDICT['pinkgorl']]

    startScreen()

    levels = readLevelsFile('starPusherLevels.txt')

    currentLevelIndex = 0

    while True:
        result = runLevel(levels, currentLevelIndex)

        if result in ('solved', 'next'):
            currentLevelIndex += 1
            if currentLevelIndex >= len(levels):
                currentLevelIndex = 0
        elif result == 'back':
            currentLevelIndex -= 1
            if currentLevelIndex < 0:
                currentLevelIndex = len(levels) - 1
        elif result == 'reset':
            pass


def runLevel(levels, levelNum):
    global currentImage
    levelObj = levels[levelNum]
    mapObj = decorateMap(levelObj['mapObj'], levelObj['startState']['player'])
    gameStateObj = copy.deepcopy(levelObj['startState'])
    mapNeedsRedraw = True
    levelSurf = BASICFONT.render('Level %s of %s ' % (levelNum + 1, len(levels)), 1, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.bottomleft = (20, WINHEIGHT - 35)
    mapWidth = len(mapObj) * TILEWIDTH
    mapHeight = (len(mapObj[0]) - 1) * (TILEHEIGHT - TILEFLOORHEIGHT) + TILEHEIGHT
    MAX_CAM_X_PAN = abs(HALF_WINHEIGHT - int(mapHeight / 2)) + TILEWIDTH
    MAX_CAM_Y_PAN = abs(HALF_WINWIDTH - int(mapWidth / 2)) + TILEHEIGHT

    levelIsComplete = False

    cameraOffsetX = 0
    cameraOffsetY = 0

    cameraUp = False
    cameraDown = False
    cameraLeft = False
    cameraRight = False

    while True:
        playerMoveTo = None
        keyPressed = False

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                keyPressed = True
                if event.key == K_LEFT:
                    playerMoveTo = LEFT
                elif event.key == K_RIGHT:
                    playerMoveTo = RIGHT
                elif event.key == K_UP:
                    playerMoveTo = UP
                elif event.key == K_DOWN:
                    playerMoveTo = DOWN

                elif event.key == K_a:
                    cameraLeft = True
                elif event.key == K_d:
                    cameraRight = True
                elif event.key == K_w:
                    cameraUp = True
                elif event.key == K_s:
                    cameraDown = True

                elif event.key == K_n:
                    return 'next'
                elif event.key == K_b:
                    return 'back'

                elif event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_BACKSPACE:
                    return 'reset'

                elif event.key == K_p:
                    currentImage += 1
                    if currentImage >= len(PLAYERIMAGES):
                        currentImage = 0
                    mapNeedsRedraw = True

            elif event.type == KEYUP:
                if event.key == K_a:
                    cameraLeft = False
                elif event.key == K_d:
                    cameraRight = False
                elif event.key == K_w:
                    cameraUp = False
                elif event.key == K_s:
                    cameraDown = False

        if playerMoveTo != None and not levelIsComplete:
            moved = makeMove(mapObj, gameStateObj, playerMoveTo)
            if moved:
                gameStateObj['stepCounter'] += 1
                mapNeedsRedraw = True
            if isLevelFinished(levelObj, gameStateObj):
                levelIsComplete = True
                keyPressed = False

        DISPLAYSURF.fill(BGCOLOR)

        if mapNeedsRedraw:
            mapSurf = drawMap(mapObj, gameStateObj, levelObj['goals'])
            mapNeedsRedraw = False

        if cameraUp and cameraOffsetY < MAX_CAM_X_PAN:
            cameraOffsetY += CAM_MOVE_SPEED
        elif cameraDown and cameraOffsetY > -MAX_CAM_X_PAN:
            cameraOffsetY -= CAM_MOVE_SPEED
        elif cameraLeft and cameraOffsetX < MAX_CAM_Y_PAN:
            cameraOffsetX += CAM_MOVE_SPEED
        elif cameraRight and cameraOffsetX > -MAX_CAM_Y_PAN:
            cameraOffsetX -= CAM_MOVE_SPEED

        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH + cameraOffsetX, HALF_WINHEIGHT + cameraOffsetY)

        DISPLAYSURF.blit(mapSurf, mapSurfRect)

        DISPLAYSURF.blit(levelSurf, levelRect)
        stepSurf = BASICFONT.render('Steps: %s' % (gameStateObj['stepCounter']), 1, TEXTCOLOR)
        stepRect = stepSurf.get_rect()
        stepRect.bottomleft = (20, WINWIDTH - 10)
        DISPLAYSURF.blit(stepSurf, stepRect)

        if levelIsComplete:
            solverRect = IMAGESDICT['solved'].get_rect()
            solverRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)
            DISPLAYSURF.blit(IMAGESDICT['solved'], solverRect)

            if keyPressed:
                return 'sovled'

        pygame.display.update()
        FPSCLOCK.tick()


def decorateMap(mapObj, startxy):
    startx, starty = startxy
    mapObjCopy = copy.deepcopy(mapObj)

    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):
            if mapObjCopy[x][y] in ('$', '.', '@', '+', '*'):
                mapObjCopy[x][y] = ' '

    floodFill(mapObjCopy, startx, starty, ' ', 'o')

    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):
            if mapObjCopy[x][y] == '#':
                if (isWall(mapObjCopy, x, y - 1) and isWall(mapObjCopy, x + 1, y)) or \
                        (isWall(mapObjCopy, x + 1, y) and isWall(mapObjCopy, x, y + 1)) or \
                        (isWall(mapObjCopy, x, y + 1) and isWall(mapObjCopy, x - 1, y)) or \
                        (isWall(mapObjCopy, x - 1, y) and isWall(mapObjCopy, x, y - 1)):
                    mapObjCopy[x][y] = 'x'
            elif mapObjCopy[x][y] == ' ' and random.randint(0, 99) < OUTSIDE_DECORATION_PCT:
                mapObjCopy[x][y] = random.choice(list(OUTSIDEDECOMAPPING.keys()))
    return mapObjCopy


def isBlocked(mapObj, gameStateObj, x, y):

    if isWall(mapObj,x,y):
        return True
    elif x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return True
    elif (x,y) in gameStateObj['stars']:
        return True

    return False


def makeMove(mapObj, gameStateObj,playerMoveTo):
    playerx,playery = gameStateObj['player']
    stars = gameStateObj['stars']
    
    if playerMoveTo == UP:
        xOffset = 0
        yOffset = -1
    elif playerMoveTo == DOWN:
        xOffset = 0
        yOffset = 1
    elif playerMoveTo == LEFT:
        xOffset = -1
        yOffset = 0
    elif playerMoveTo == RIGHT:
        xOffset = 1
        yOffset = 0
    
    if isWall(mapObj,playerx+xOffset,playery+yOffset):
        return False
    else:
        if (playerx+xOffset,playery+yOffset) in stars:
            if not isBlocked(mapObj,gameStateObj,playerx+(xOffset*2),playery+(yOffset*2)):
                ind = stars.index((playerx+xOffset,playery+yOffset))
                stars[ind] = (stars[ind][0]+xOffset,stars[ind][1]+yOffset)
            else:
                return False
        
        gameStateObj['player'] = (playerx+xOffset,playery+yOffset)
        return True



def isLevelFinished(levelObj, gameStateObj):
    for goal in levelObj['goals']:
        if goal not in gameStateObj['stars']:
            return False
    return True


def drawMap(mapObj, gameStateObj, goals):
    mapSurfWidth = len(mapObj) * TILEWIDTH
    mapSurfHeight = (len(mapObj[0]) - 1) * (TILEHEIGHT - TILEFLOORHEIGHT) + TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR)

    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            spaceRect = pygame.Rect((x * TILEWIDTH, y * (TILEHEIGHT - TILEFLOORHEIGHT), TILEWIDTH, TILEHEIGHT))
            if mapObj[x][y] in TILEMAPPING:
                baseTile = TILEMAPPING[mapObj[x][y]]
            elif mapObj[x][y] in OUTSIDEDECOMAPPING:
                baseTile = TILEMAPPING[' ']

            mapSurf.blit(baseTile, spaceRect)

            if mapObj[x][y] in OUTSIDEDECOMAPPING:
                mapSurf.blit(OUTSIDEDECOMAPPING[mapObj[x][y]], spaceRect)
            elif (x, y) in gameStateObj['stars']:
                if (x, y) in goals:
                    mapSurf.blit(IMAGESDICT['covered goal'], spaceRect)
                mapSurf.blit(IMAGESDICT['star'], spaceRect)
            elif (x, y) in goals:
                mapSurf.blit(IMAGESDICT['uncovered goal'], spaceRect)

            if (x, y) == gameStateObj['player']:
                mapSurf.blit(PLAYERIMAGES[currentImage], spaceRect)
    return mapSurf


def floodFill(mapObj, x, y, oldCharacter, newCharacter):
    if mapObj[x][y] == oldCharacter:
        mapObj[x][y] = newCharacter

    if x < len(mapObj) - 1 and mapObj[x + 1][y] == oldCharacter:
        floodFill(mapObj, x + 1, y, oldCharacter, newCharacter)
    if x > 0 and mapObj[x - 1][y] == oldCharacter:
        floodFill(mapObj, x - 1, y, oldCharacter, newCharacter)
    if y < len(mapObj[x]) - 1 and mapObj[x][y + 1] == oldCharacter:
        floodFill(mapObj, x, y + 1, oldCharacter, newCharacter)
    if y > 0 and mapObj[x][y - 1] == oldCharacter:
        floodFill(mapObj, x, y - 1, oldCharacter, newCharacter)


def isWall(mapObj, x, y):
    if x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return False
    elif mapObj[x][y] in ('#', 'x'):
        return True
    return False


def startScreen():
    titleRect = IMAGESDICT['title'].get_rect()
    topCoord = 50
    titleRect.top = topCoord
    titleRect.centerx = HALF_WINWIDTH
    topCoord += titleRect.height

    instructionText = ['Push the stars over the marks.',
                       'Arrow keys to move, WASD for ceamera control, P to change character.',
                       'Backspace to reset level, Esc to quit.',
                       'N for next level, B to go back a level.']

    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(IMAGESDICT['title'], titleRect)

    for i in range(len(instructionText)):
        instSurf = BASICFONT.render(instructionText[i], 1, TEXTCOLOR)
        instRect = instSurf.get_rect()
        topCoord += 10
        instRect.top = topCoord
        instRect.centerx = HALF_WINWIDTH
        topCoord += instRect.height
        DISPLAYSURF.blit(instSurf, instRect)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

        pygame.display.update()
        FPSCLOCK.tick()


def readLevelsFile(filename):
    assert os.path.exists(filename), 'Cannot find the level file: %s' % (filename)
    with open(filename, 'r') as mapFile:
        content = mapFile.readlines() + ['\r\n']

    levels = []
    levelNum = 0
    mapTextLines = []
    mapObj = []

    for lineNum in range(len(content)):
        line = content[lineNum].rstrip('\r\n')

        if ';' in line:
            # 忽略;行，注释行，不要
            line = line[:line.find(';')]

        if line != '':
            mapTextLines.append(line)
        elif line == '' and len(mapTextLines) > 0:
            maxWidth = -1
            for i in range(len(mapTextLines)):
                if len(mapTextLines[i]) > maxWidth:
                    maxWidth = len(mapTextLines[i])

            for i in range(len(mapTextLines)):
                mapTextLines[i] += ' ' * (maxWidth - len(mapTextLines[i]))

            for x in range(len(mapTextLines[0])):
                mapObj.append([])
            for y in range(len(mapTextLines)):
                for x in range(maxWidth):
                    mapObj[x].append(mapTextLines[y][x])

            startx = None
            starty = None
            goals = []
            stars = []

            for x in range(maxWidth):
                for y in range(len(mapObj[x])):
                    if mapObj[x][y] in ('@', '+'):
                        startx = x
                        starty = y
                    if mapObj[x][y] in ('.', '+', '*'):
                        goals.append((x, y))
                    if mapObj[x][y] in ('$', '*'):
                        stars.append((x, y))

            assert startx != None and starty != None, 'Level %s (around line %s) in %s is missing a "@" or "+" to mark the start point.' % (
                levelNum + 1, lineNum, filename)
            assert len(goals) > 0, 'Level %s (around line %s) in %s must have at least one goal.' % (
                levelNum + 1, lineNum, filename)
            assert len(stars) >= len(
                goals), 'Level %s (around line %s) in %s is impossible to solve.It has %s goals but only %s stars.' % (
                levelNum + 1, lineNum, filename, len(goals), len(stars))

            gameStateObj = {'player': (startx, starty),
                            'stepCounter': 0,
                            'stars': stars}
            levelObj = {'width': maxWidth,
                        'height': len(mapObj),
                        'mapObj': mapObj,
                        'goals': goals,
                        'startState': gameStateObj}

            levels.append(levelObj)

            mapTextLines = []
            mapObj = []
            gameStateObj = []
            lineNum += 1
    return levels


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
