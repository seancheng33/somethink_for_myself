'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/6/19
@Program      : pygame练习，做一个答题的程序，有游戏的标题界面
                使用数字键1-4作答，在答题界面按回退键可以返回标题界面。
                按enter键进入下一题。有一个计时器，每题的答题都会倒计时。
'''
import sys
import pygame
from pygame.locals import *


def game_title():
    start_text = '请按 空格 键开始游戏'

    title_image = titleFont.render('Title Game Name', True, color_dict['green'])
    tips_image = globalFont.render(start_text, True, color_dict['orange'])
    SUBFACE.blit(title_image, (50, 50))
    SUBFACE.blit(tips_image, (300, 400))
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
                elif event.key == K_SPACE:
                    # 按下开始键开始游戏
                    load_game(0)
                    return

        pygame.display.update()
        pygame.time.Clock().tick()


def load_game(leves):
    SUBFACE.fill(color_dict['black'])
    level = game_level[leves]
    level_question = level['question']
    level_answer = level['answer']
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
        pygame.time.Clock().tick()


def input_handle(number, correct):
    if number == correct:
        text = globalFont.render('答案正确', True, color_dict['green'])
    else:
        text = globalFont.render('答案错误', True, color_dict['red'])
    return SUBFACE.blit(text, (50, 550))


def main():
    global SUBFACE, titleFont, globalFont, color_dict, game_level
    color_dict = {'red': (255, 0, 0),  # 纯红
                  'blue': (255, 0, 0),  # 纯蓝
                  'green': (0, 125, 0),  # 纯绿
                  'lime': (0, 255, 0),  # 酸橙色
                  'gold': (255, 215, 0),  # 金色
                  'orange': (255, 165, 0),  # 橙色
                  'black': (0, 0, 0),  # 纯黑
                  'white': (255, 255, 255),  # 纯白
                  }

    game_level = [
        {'question': '以下哪一个是Python合法的标识符？', 'answer': ['_name', '1name', 'stu-name', 'stu.name'], 'correct': 1},
        {'question': '以下不能作为字典的key的是哪一个选项？', 'answer': ['2016', '\'china\'', 'listA=[\'Name\']', 'tupleA=(123)'], 'correct': 3},
        {'question': '问题03，', 'answer': ['答案A', '答案B', '答案C', '答案D'], 'correct': 1},
        {'question': '问题04，', 'answer': ['答案E', '答案F', '答案G', '答案H'], 'correct': 4}
    ]

    #
    pygame.init()
    SUBFACE = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('答题游戏 version 1.0 Demo')

    titleFont = pygame.font.SysFont('SimHei', 60)
    globalFont = pygame.font.SysFont('SimHei', 36)
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
        pygame.time.Clock().tick()


if __name__ == '__main__':
    main()
