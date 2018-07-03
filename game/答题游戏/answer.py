'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/6/19
@Program      : pygame练习，做一个答题的程序，有游戏的标题界面，鼠标选择答案的形式作答，题库使用xml文件的形式。
'''
import random
import sys

import pygame
from pygame.locals import *
from xml.dom.minidom import parse


def game_title():
    title_text = '大脑 很囧'
    bt_start_text = '开 始 游 戏'
    bt_about_text = '关 于 游 戏'
    title_bg = pygame.image.load('img/main.jpg')
    title_image = titleFont.render(title_text, True, color_dict['green'])
    title_time = 0
    mouseCursor = pygame.image.load('img/cursor.png').convert_alpha()  # 加载鼠标图片
    while True:
        SUBFACE.blit(title_bg, (0, 0))
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
                close_program()
            elif event.type == KEYDOWN:
                # 按键按下后抬起的事件判断
                if event.key == K_ESCAPE:
                    close_program()

        x, y = pygame.mouse.get_pos()
        pressed_array = pygame.mouse.get_pressed()  # 获取鼠标事件的列表

        # 开始按键的鼠标事件，包括了鼠标经过事件和点击事件
        if tips_rect.left < x < tips_rect.right and tips_rect.top < y < tips_rect.bottom:
            tips_image = globalFont.render(bt_start_text, True, color_dict['red'])
            SUBFACE.blit(tips_image, tips_rect)

            for event in pressed_array:
                if event == 1:  # 1为鼠标左键点击事件
                    return 'start'

        # 关于按键的鼠标事件
        if help_rect.left < x < help_rect.right and help_rect.top < y < help_rect.bottom:
            help_image = globalFont.render(bt_about_text, True, color_dict['red'])
            SUBFACE.blit(help_image, help_rect)
            for event in pressed_array:
                if event == 1:  # 1为鼠标左键点击事件
                    return 'about'

        # 自定义鼠标样式
        pygame.mouse.set_visible(False)

        x -= 0
        y -= 0

        SUBFACE.blit(mouseCursor, (x, y))
        pygame.display.update()
        pygame.time.Clock().tick(30)


def load_game(levels, total_score, total_right_score, total_wrong_score):
    SUBFACE.fill(color_dict['black'])
    title_bg = pygame.image.load('img/title.jpg')

    level = game_level[levels]
    level_question = level['question']
    level_answer = level['answers']
    level_correct = int(level['correct'])

    mouseCursor = pygame.image.load('img/cursor.png').convert_alpha()

    while True:

        SUBFACE.blit(title_bg, (0, 0))

        # 显示出问题,按照宽度是25个字符串的规格显示出来。
        for i in range(int(len(level_question) / 25 + 1)):
            start = i * 25
            end = (i + 1) * 25
            question_image = questionFont.render(level_question[start:end], True, color_dict['black'])
            SUBFACE.blit(question_image, (50, 80 + (i * 30)))

        # 右侧的内容
        level_image = helpFont.render('当前题目：第 ' + str(levels + 1) + ' 题', True, color_dict['orange'])
        SUBFACE.blit(level_image, (725, 80))
        score_image = helpFont.render('当前分数：' + str(total_score), True, color_dict['orange'])
        SUBFACE.blit(score_image, (725, 120))
        score_image = helpFont.render('正确题数：' + str(total_right_score), True, color_dict['orange'])
        SUBFACE.blit(score_image, (725, 160))
        score_image = helpFont.render('错误题数：' + str(total_wrong_score), True, color_dict['orange'])
        SUBFACE.blit(score_image, (725, 200))

        # 显示出答案选项
        item1_image = answerFont.render('1 - ' + level_answer[0], True, color_dict['red'])
        item1_rect = item1_image.get_rect()
        item1_rect.left = 50
        item1_rect.top = 280
        item2_image = answerFont.render('2 - ' + level_answer[1], True, color_dict['red'])
        item2_rect = item2_image.get_rect()
        item2_rect.left = 50
        item2_rect.top = 350
        item3_image = answerFont.render('3 - ' + level_answer[2], True, color_dict['red'])
        item3_rect = item3_image.get_rect()
        item3_rect.left = 50
        item3_rect.top = 420
        item4_image = answerFont.render('4 - ' + level_answer[3], True, color_dict['red'])
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
                close_program()
            elif event.type == KEYDOWN:
                # 按键按下后抬起的事件判断
                if event.key == K_ESCAPE:
                    close_program()
                elif event.key == K_BACKSPACE:
                    # 按回退键，返回到标题界面。
                    return 'reset'
                elif event.key == K_RETURN:
                    # 按回车键，跳到下一题。
                    return 'next'

        # 鼠标控制事件
        x, y = pygame.mouse.get_pos()
        # 四个答案区域的内容的鼠标鼠标时间控制
        if item1_rect.left < x < item1_rect.right and item1_rect.top < y < item1_rect.bottom:
            item1_image = answerFont.render('1 - ' + level_answer[0], True, color_dict['gold'])
            SUBFACE.blit(item1_image, item1_rect)
            pressed = pygame.mouse.get_pressed()
            for event in pressed:
                if event == 1:
                    pygame.time.wait(1000)  # 等待一秒，防止点击太快变成连下一题也点了
                    if level_correct == 1:
                        return 'yes'
                    else:
                        return 'no'
        if item2_rect.left < x < item2_rect.right and item2_rect.top < y < item2_rect.bottom:
            item2_image = answerFont.render('2 - ' + level_answer[1], True, color_dict['gold'])
            SUBFACE.blit(item2_image, item2_rect)
            pressed = pygame.mouse.get_pressed()
            for event in pressed:
                if event == 1:
                    pygame.time.wait(1000)  # 等待一秒，防止点击太快变成连下一题也点了
                    if level_correct == 2:
                        return 'yes'
                    else:
                        return 'no'
        if item3_rect.left < x < item3_rect.right and item3_rect.top < y < item3_rect.bottom:
            item3_image = answerFont.render('3 - ' + level_answer[2], True, color_dict['gold'])
            SUBFACE.blit(item3_image, item3_rect)
            pressed = pygame.mouse.get_pressed()
            for event in pressed:
                if event == 1:
                    pygame.time.wait(1000)  # 等待一秒，防止点击太快变成连下一题也点了
                    if level_correct == 3:
                        return 'yes'
                    else:
                        return 'no'
        if item4_rect.left < x < item4_rect.right and item4_rect.top < y < item4_rect.bottom:
            item4_image = answerFont.render('4 - ' + level_answer[3], True, color_dict['gold'])
            SUBFACE.blit(item4_image, item4_rect)
            pressed = pygame.mouse.get_pressed()
            for event in pressed:
                if event == 1:
                    pygame.time.wait(1000)  # 等待一秒，防止点击太快变成连下一题也点了
                    if level_correct == 4:
                        return 'yes'
                    else:
                        return 'no'
        # 右侧按键的鼠标事件

        # 自定义鼠标样式
        pygame.mouse.set_visible(False)
        x -= 0
        y -= 0
        SUBFACE.blit(mouseCursor, (x, y))

        pygame.display.update()
        pygame.time.Clock().tick(60)


def end_game(score, right_score, wrong_score):
    # 游戏的结束界面，对刚才完过的游戏做出一些数据统计。
    score_img = globalFont.render('最终总成绩： ' + str(score), True, color_dict['orange'])
    score_rect = score_img.get_rect()
    score_rect.top = 100
    score_rect.centerx = SUBFACE.get_rect().centerx

    total_right_percent = right_score / (right_score + wrong_score)
    right_img = globalFont.render('正确率： ' + str(total_right_percent*100) + ' %', True, color_dict['orange'])
    right_rect = right_img.get_rect()
    right_rect.top = 150
    right_rect.centerx = SUBFACE.get_rect().centerx

    right_score_img = globalFont.render('正确题数： ' + str(right_score), True, color_dict['orange'])
    right_score_rect = right_score_img.get_rect()
    right_score_rect.top = 200
    right_score_rect.centerx = SUBFACE.get_rect().centerx

    bg_img = pygame.image.load('img/end_bg.jpg').convert_alpha()
    bg_rect = bg_img.get_rect()
    bg_rect.center = SUBFACE.get_rect().center

    bg_fill = pygame.Rect((0, 0), (400, 500))
    bg_fill.center = SUBFACE.get_rect().center

    while True:
        SUBFACE.blit(bg_img, bg_rect)
        pygame.draw.rect(SUBFACE, (255, 255, 255, 80), bg_fill)
        pygame.draw.rect(SUBFACE, (0, 0, 0), bg_fill, 2)
        SUBFACE.blit(score_img, score_rect)
        SUBFACE.blit(right_score_img, right_score_rect)
        SUBFACE.blit(right_img, right_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                close_program()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    close_program()
                elif event.key == K_RETURN:
                    return 'reset'

        pygame.display.update()
        pygame.time.Clock().tick(60)


def about_this():
    pass


def close_program():
    pygame.quit()
    sys.exit(0)


def load_file(filename):
    # 读取xml文件中的题库
    question_data = parse(filename)
    # 得到根节点
    root = question_data.documentElement

    game_level = []
    questions = root.getElementsByTagName("question")

    for item in questions:
        q_list = {}
        answerList = []
        question = item.getAttribute("title")
        answer_items = item.getElementsByTagName("answer")  # 返回一个列表
        answerList.append(answer_items[0].getElementsByTagName("a")[0].childNodes[0].data)
        answerList.append(answer_items[0].getElementsByTagName("b")[0].childNodes[0].data)
        answerList.append(answer_items[0].getElementsByTagName("c")[0].childNodes[0].data)
        answerList.append(answer_items[0].getElementsByTagName("d")[0].childNodes[0].data)
        correct = item.getElementsByTagName("correct")[0].childNodes[0].data
        q_list['question'] = question
        q_list['answers'] = answerList
        q_list['correct'] = correct
        game_level.append(q_list)


    # 生产随机指定数量的题集
    tmp_level = set()
    while len(tmp_level) < 10:
        randNum = random.randint(0, len(game_level)-1)
        tmp_level.add(randNum)

    new_question = []
    for i in tmp_level:
        new_question.append(game_level[i])

    # 因为set的缘故，提取出来的题目是安装顺序排列的，需要在打乱一次
    random.shuffle(new_question)

    return new_question


def main():
    # 全局话声明
    global SUBFACE, titleFont, globalFont, helpFont, color_dict, game_level, questionFont, answerFont, score, right_score, wrong_score

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
    pygame.display.set_icon(pygame.image.load('img/delbrucks-brain.ico'))
    pygame.display.set_caption('大脑很囧--答题类游戏 Version 1.0.0')

    titleFont = pygame.font.Font('font/YaHei.ttf', 150)
    globalFont = pygame.font.Font('font/YaHei.ttf', 36)
    questionFont = pygame.font.Font('font/huakan.ttf', 24)
    answerFont = pygame.font.Font('font/huakan.ttf', 22)
    helpFont = pygame.font.Font('font/huakan.ttf', 24)
    result = game_title()
    corrent = 0
    score = 0
    right_score = 0
    wrong_score = 0
    while True:
        if 'reset' in result:
            corrent = 0
            result = game_title()
        elif 'start' in result:
            result = load_game(corrent, score, right_score, wrong_score)
        elif 'about' in result:
            pass
        elif result in ('next', 'yes', 'no'):
            if result in 'yes':
                score += 100
                right_score += 1
            elif result in 'no':
                wrong_score += 1

            # 先计分，否则最后的统计会出错
            if corrent == len(game_level) - 1:
                result = end_game(score, right_score, wrong_score)
            else:
                corrent += 1
                result = load_game(corrent, score, right_score, wrong_score)
        else:
            pass

        pygame.display.update()
        pygame.time.Clock().tick(60)


if __name__ == '__main__':
    main()
