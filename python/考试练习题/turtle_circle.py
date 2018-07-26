'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/7/26 
@Program       : turtle 绘制蓝色圆形
'''

import turtle

turtle.setup(600, 600)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()
turtle.done()
