'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/10
@Program      : 模拟自页游大航海时代5的投资功能的小游戏。首先显示三张牌，然后再从剩下的牌中，
                抽出牌组合，总点数为9点即最高牌点组合，如果超过10点为失败。牌数一个10张。
'''
import random
import sys
import pygame
from pygame.locals import *


def addCardAnimation():
    pass


def main():
    SCREENWIDTH = 800
    SCREEBHEIGHT = 480
    pygame.init()
    SCREENFACE = pygame.display.set_mode((SCREENWIDTH, SCREEBHEIGHT))
    pygame.display.set_caption('Poker Game Ver 0.1.1')

    srcImage = pygame.image.load('img/number.png').convert_alpha()

    CARDSIZE = (130, 180)
    IMAGEDICTS={'NUM0': srcImage.subsurface((1, 0), CARDSIZE),
                'NUM1': srcImage.subsurface((170, 0), CARDSIZE),
                'NUM2': srcImage.subsurface((334, 0), CARDSIZE),
                'NUM3': srcImage.subsurface((502, 0), CARDSIZE),
                'NUM4': srcImage.subsurface((670, 0), CARDSIZE),
                'NUM5': srcImage.subsurface((1, 209), CARDSIZE),
                'NUM6': srcImage.subsurface((170, 209), CARDSIZE),
                'NUM7': srcImage.subsurface((334, 209), CARDSIZE),
                'NUM8': srcImage.subsurface((502, 209), CARDSIZE),
                'NUM9': srcImage.subsurface((670, 209), CARDSIZE)
                }

    CARD = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(CARD)

    FPSCLOCK = pygame.time.Clock()
    FPS = 30

    cardSelected = 0

    while True:
        SCREENFACE.fill((0, 125, 0))

        SCREENFACE.blit(IMAGEDICTS['NUM'+str(CARD[0])], (80, 50))
        SCREENFACE.blit(IMAGEDICTS['NUM'+str(CARD[1])], (280, 50))
        SCREENFACE.blit(IMAGEDICTS['NUM'+str(CARD[2])], (480, 50))

        x, y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        card_rect1 = IMAGEDICTS['NUM'+str(CARD[0])].get_rect()
        card_rect1.topleft = (80, 50)
        card_rect2 = IMAGEDICTS['NUM' + str(CARD[1])].get_rect()
        card_rect2.topleft = (280, 50)
        card_rect3 = IMAGEDICTS['NUM' + str(CARD[2])].get_rect()
        card_rect3.topleft = (480, 50)

        if cardSelected == 1:
            pygame.draw.rect(SCREENFACE, (255, 0, 0), card_rect1, 4)
        elif cardSelected == 2:
            pygame.draw.rect(SCREENFACE, (255, 0, 0), card_rect2, 4)
        elif cardSelected == 3:
            pygame.draw.rect(SCREENFACE, (255, 0, 0), card_rect3, 4)

        if card_rect1.collidepoint(x, y):
            for event in pressed:
                if event == 1:
                    if cardSelected == 0:
                        cardSelected = 1
                    else:
                        pass

        if card_rect2.collidepoint(x, y):
            for event in pressed:
                if event == 1:
                    if cardSelected == 0:
                        cardSelected = 2
                    else:
                        pass

        if card_rect3.collidepoint(x, y):
            for event in pressed:
                if event == 1:
                    if cardSelected == 0:
                        cardSelected = 3
                    else:
                        pass

        addCardAnimation()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
