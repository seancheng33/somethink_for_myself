'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/6/19
@Program      : pygame练习，做一个答题的程序，有游戏的标题界面
                使用数字键1-4作答，在答题界面按回退键可以返回标题界面。
                按enter键进入下一题。有一个计时器，每题的答题都会倒计时。
                题库使用xml文件的形式
'''
import sys

import pygame
from pygame.locals import *
from xml.dom.minidom import parse


def game_title():
    title_text = '答题游戏标题'
    start_text = '开始游戏'
    about_text = '基于python3.6.4和pygame制作。'
    title_bg = pygame.image.load('img/bg.jpg')
    SUBFACE.blit(title_bg, (0, 0))
    # SUBFACE.fill(color_dict['black'])
    title_image = titleFont.render(title_text, True, color_dict['white'])
    # tips_image = globalFont.render(start_text, True, color_dict['orange'])

    help_image = helpFont.render(about_text, True, color_dict['white'])

    while True:
        tips_image = globalFont.render(start_text, True, color_dict['orange'])
        tips_rect = tips_image.get_rect()

        SUBFACE.blit(title_image, (230, 150))
        SUBFACE.blit(tips_image, (285, 400))
        SUBFACE.blit(help_image, (240, 500))

        for event in pygame.event.get():
            # 关闭按钮的事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == KEYUP:
                # 按键按下后抬起的事件判断
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                elif event.key == K_SPACE:
                    # 按下开始键开始游戏
                    load_game(0)
                    return
            elif event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 285 < x < 285 + tips_rect.right and 400 < y < 400 + tips_rect.bottom:
                    load_game(0)
                return

        x, y = pygame.mouse.get_pos()

        if 285 < x < 285 + tips_rect.right and 400 < y < 400 + tips_rect.bottom:
            tips_image = globalFont.render(start_text, True, color_dict['red'])
            SUBFACE.blit(tips_image, (285, 400))

        pygame.display.update()
        pygame.time.Clock().tick(30)


def load_game(levels):
    SUBFACE.fill(color_dict['black'])
    level = game_level[levels]
    level_question = level['question']
    level_answer = level['answers']
    level_correct = int(level['correct'])

    # 显示出问题
    question_image = globalFont.render(level_question, True, color_dict['green'])
    SUBFACE.blit(question_image, (50, 150))
    # 显示出答案

    item1_image = globalFont.render('1 - '+level_answer[0], True, color_dict['gold'])
    SUBFACE.blit(item1_image, (50, 250))
    item2_image = globalFont.render('2 - '+level_answer[1], True, color_dict['gold'])
    SUBFACE.blit(item2_image, (50, 300))
    item3_image = globalFont.render('3 - '+level_answer[2], True, color_dict['gold'])
    SUBFACE.blit(item3_image, (50, 350))
    item4_image = globalFont.render('4 - '+level_answer[3], True, color_dict['gold'])
    SUBFACE.blit(item4_image, (50, 400))

    while True:

        for event in pygame.event.get():
            # 关闭按钮的事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == KEYUP:
                # 按键按下后抬起的事件判断
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                elif event.key == K_1:
                    answer_text = input_handle(1, level_correct)
                elif event.key == K_2:
                    answer_text = input_handle(2, level_correct)
                elif event.key == K_3:
                    answer_text = input_handle(3, level_correct)
                elif event.key == K_4:
                    answer_text = input_handle(4, level_correct)
                elif event.key == K_BACKSPACE:
                    # 按回退键，返回到标题界面。
                    return 'reset'
                elif event.key == K_RETURN:
                    return 'next'


        pygame.display.update()
        pygame.time.Clock().tick(30)


def input_handle(number, correct):
    if number == correct:
        text = globalFont.render('答案正确', True, color_dict['green'])
    else:
        text = globalFont.render('答案错误', True, color_dict['red'])
    return SUBFACE.blit(text, (50, 550))


def load_file(filename):
    question_data = parse(filename)
    # 得到根节点
    root = question_data.documentElement

    game_level = []
    questions = root.getElementsByTagName("question")
    # print(questions)
    for item in questions:
        list ={}
        question = item.getAttribute("title")
        answer_items = item.getElementsByTagName("answer")  # 返回一个列表
        answers = []
        answers.append(answer_items[0].getElementsByTagName("a")[0].childNodes[0].data)
        answers.append(answer_items[0].getElementsByTagName("b")[0].childNodes[0].data)
        answers.append(answer_items[0].getElementsByTagName("c")[0].childNodes[0].data)
        answers.append(answer_items[0].getElementsByTagName("d")[0].childNodes[0].data)
        correct = item.getElementsByTagName("correct")[0].childNodes[0].data
        list['question'] = question
        list['answers'] = answers
        list['correct'] = correct
        game_level.append(list)

    return game_level

def main():
    global SUBFACE, titleFont, globalFont, helpFont, color_dict, game_level
    color_dict = {'red': (255, 0, 0),  # 纯红
                  'blue': (255, 0, 0),  # 纯蓝
                  'green': (0, 125, 0),  # 纯绿
                  'lime': (0, 255, 0),  # 酸橙色
                  'gold': (255, 215, 0),  # 金色
                  'orange': (255, 165, 0),  # 橙色
                  'black': (0, 0, 0),  # 纯黑
                  'white': (255, 255, 255),  # 纯白
                  }

    game_level = load_file("data.xml")

    #
    pygame.init()
    SUBFACE = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('答题游戏 version 1.0 Demo')

    titleFont = pygame.font.Font('font/YaHei.ttf', 60)
    globalFont = pygame.font.Font('font/YaHei.ttf', 36)
    helpFont = pygame.font.Font('font/YaHei.ttf', 24)
    game_title()
    corrent = 0
    while True:
        result = load_game(corrent)

        if result == 'reset':
            corrent = 0
            game_title()
        elif result == 'next':
            if corrent == len(game_level)-1:
                corrent = 0
            else:
                corrent += 1
            load_game(corrent)

        pygame.display.update()
        pygame.time.Clock().tick(30)


if __name__ == '__main__':
    main()
