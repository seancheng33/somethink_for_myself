'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/6/19
@Program      : pygame练习，做一个答题的程序，有游戏的标题界面
                使用数字键1-4作答，在答题界面按回退键可以返回标题界面。
                按enter键进入下一题。有一个计时器，每题的答题都会倒计时。
                题库使用xml文件的形式
                后续优化思路：1、使用shelve做题库的数据存储和读取。
                            2、多题，随机取出一定数量的题目，进行游戏
                            3、本脚本项目化，形成比较正规的项目结构
'''
import sys

import pygame
from pygame.locals import *
from xml.dom.minidom import parse


def game_title():
    title_text = '大脑 很囧'
    bt_start_text = '开 始 游 戏'
    bt_about_text = '关 于 游 戏'
    title_bg = pygame.image.load('img/main.jpg')
    SUBFACE.blit(title_bg, (0, 0))

    title_time = 0
    while True:
        if title_time == 0:
            title_image = titleFont.render(title_text, True, color_dict['white'])
            title_time = 1
        elif title_time == 1:
            title_image = titleFont.render(title_text, True, color_dict['green'])
            title_time = 2
        elif title_time == 2:
            title_image = titleFont.render(title_text, True, color_dict['lime'])
            title_time = 0
        title_rect = title_image.get_rect()
        title_rect.centerx = SUBFACE.get_rect().centerx
        title_rect.top = 130

        tips_image = globalFont.render(bt_start_text, True, color_dict['orange'])
        tips_rect = tips_image.get_rect()
        tips_rect.centerx = SUBFACE.get_rect().centerx - 150
        tips_rect.top = 400

        help_image = globalFont.render(bt_about_text, True, color_dict['orange'])
        help_rect = help_image.get_rect()
        help_rect.centerx = SUBFACE.get_rect().centerx + 150
        help_rect.top = 400

        SUBFACE.blit(title_image, title_rect)
        SUBFACE.blit(tips_image, tips_rect)
        SUBFACE.blit(help_image, help_rect)

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

        x, y = pygame.mouse.get_pos()
        # 开始按键的鼠标事件，包括了鼠标经过事件和点击事件
        if tips_rect.left < x < tips_rect.right and tips_rect.top < y < tips_rect.bottom:
            tips_image = globalFont.render(bt_start_text, True, color_dict['red'])
            SUBFACE.blit(tips_image, tips_rect)
            pressed_array = pygame.mouse.get_pressed()  # 获取鼠标事件的列表
            for event in pressed_array:
                if event == 1:  # 1为鼠标左键点击事件
                    load_game(0)
                    return

        if help_rect.left < x < help_rect.right and help_rect.top < y < help_rect.bottom:
            help_image = globalFont.render(bt_about_text, True, color_dict['red'])
            SUBFACE.blit(help_image, help_rect)

        pygame.display.update()
        pygame.time.Clock().tick(30)


def load_game(levels):
    SUBFACE.fill(color_dict['black'])
    title_bg = pygame.image.load('img/title.jpg')
    SUBFACE.blit(title_bg, (0, 0))
    level = game_level[levels]
    level_question = level['question']
    level_answer = level['answers']
    level_correct = int(level['correct'])

    tips_text = ['用鼠标选择答案','']
    score = 0


    # 右侧的各种选项的显示，包括说明，分数，当前第几题。

    # 显示出问题
    question_image = questionFont.render(level_question, True, color_dict['black'])
    SUBFACE.blit(question_image, (50, 100))

    while True:
        # 右侧的内容
        level_image = helpFont.render('当前题目：第 '+str(levels+1)+' 题', True, color_dict['orange'])
        SUBFACE.blit(level_image, (725, 80))
        score_image = helpFont.render('当前分数：'+str(score), True, color_dict['orange'])
        SUBFACE.blit(score_image, (725, 120))
        score_image = helpFont.render('正确题数：'+str(score), True, color_dict['orange'])
        SUBFACE.blit(score_image, (725, 160))
        score_image = helpFont.render('错误题数：'+str(score), True, color_dict['orange'])
        SUBFACE.blit(score_image, (725, 200))
        # 显示出答案选项
        item1_image = answerFont.render('1 - ' + level_answer[0], True, color_dict['gold'])
        item1_rect = item1_image.get_rect()
        item1_rect.left = 50
        item1_rect.top = 280
        item2_image = answerFont.render('2 - ' + level_answer[1], True, color_dict['gold'])
        item2_rect = item2_image.get_rect()
        item2_rect.left = 50
        item2_rect.top = 350
        item3_image = answerFont.render('3 - ' + level_answer[2], True, color_dict['gold'])
        item3_rect = item3_image.get_rect()
        item3_rect.left = 50
        item3_rect.top = 420
        item4_image = answerFont.render('4 - ' + level_answer[3], True, color_dict['gold'])
        item4_rect = item4_image.get_rect()
        item4_rect.left = 50
        item4_rect.top = 490

        SUBFACE.blit(item1_image, item1_rect)
        SUBFACE.blit(item2_image, item2_rect)
        SUBFACE.blit(item3_image, item3_rect)
        SUBFACE.blit(item4_image, item4_rect)

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
                elif event.key == K_BACKSPACE:
                    # 按回退键，返回到标题界面。
                    return 'reset'
                elif event.key == K_RETURN:

                    return 'next'

        # 鼠标控制事件
        x, y = pygame.mouse.get_pos()

        if item1_rect.left < x < item1_rect.right and item1_rect.top < y < item1_rect.bottom:
            item1_image = answerFont.render('1 - ' + level_answer[0], True, color_dict['white'])
            SUBFACE.blit(item1_image, item1_rect)
        if item2_rect.left < x < item2_rect.right and item2_rect.top < y < item2_rect.bottom:
            item2_image = answerFont.render('2 - ' + level_answer[1], True, color_dict['white'])
            SUBFACE.blit(item2_image, item2_rect)
        if item3_rect.left < x < item3_rect.right and item3_rect.top < y < item3_rect.bottom:
            item3_image = answerFont.render('3 - ' + level_answer[2], True, color_dict['white'])
            SUBFACE.blit(item3_image, item3_rect)
        if item4_rect.left < x < item4_rect.right and item4_rect.top < y < item4_rect.bottom:
            item4_image = answerFont.render('4 - ' + level_answer[3], True, color_dict['white'])
            SUBFACE.blit(item4_image, item4_rect)

        pygame.display.update()
        pygame.time.Clock().tick(60)


def load_file(filename):
    question_data = parse(filename)
    # 得到根节点
    root = question_data.documentElement

    game_level = []
    questions = root.getElementsByTagName("question")
    # print(questions)
    for item in questions:
        list = {}
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
    # 全局话声明
    global SUBFACE, titleFont, globalFont, helpFont, color_dict, game_level, questionFont, answerFont

    # 颜色字典
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

    # 初始化
    pygame.init()
    SUBFACE = pygame.display.set_mode((1024, 640))
    pygame.display.set_caption('答题游戏 version 1.0 Demo')

    titleFont = pygame.font.Font('font/YaHei.ttf', 150)
    globalFont = pygame.font.Font('font/YaHei.ttf', 36)
    questionFont = pygame.font.Font('font/huakan.ttf', 24)
    answerFont = pygame.font.Font('font/huakan.ttf', 24)
    helpFont = pygame.font.Font('font/huakan.ttf', 24)
    game_title()
    corrent = 0

    while True:
        result = load_game(corrent)

        if 'reset' in result:
            corrent = 0
            game_title()
        elif 'next' in result:
            if corrent == len(game_level) - 1:
                corrent = 0
            else:
                corrent += 1
            load_game(corrent)
        elif result == '':
            pass

        pygame.display.update()
        pygame.time.Clock().tick(60)


if __name__ == '__main__':
    main()
