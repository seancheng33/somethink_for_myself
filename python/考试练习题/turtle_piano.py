'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/7/27
@Program       : turtle 绘制黑白的钢琴图形
'''

import turtle as t

t.setup(500,300)
t.penup()
t.goto(-180,-50)
t.pendown()
def Drawrect():
    t.fd(40)
    t.left(90)
    t.fd(120)
    t.left(90)
    t.fd(40)
    t.left(90)
    t.fd(120)
    t.penup()
    t.left(90)
    t.fd(42)
    t.pendown()

for i in range(7):
    Drawrect()
t.penup()
t.goto(-150,0)
t.pendown()
def DrawRectBlack():
    t.color('black')
    t.begin_fill()
    t.fd(30)
    t.left(90)
    t.fd(70)
    t.left(90)
    t.fd(30)
    t.left(90)
    t.fd(70)
    t.end_fill()
    t.penup()
    t.left(90)
    t.fd(40)
    t.pendown()
DrawRectBlack()
DrawRectBlack()
t.penup()
t.fd(48)
DrawRectBlack()
DrawRectBlack()
DrawRectBlack()
t.hideturtle()
t.done()
