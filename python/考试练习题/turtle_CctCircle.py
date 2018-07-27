'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/7/27
@Program       : turtle 绘制同心圆
'''

import turtle as t

def DrawCctCircle(n):
    t.penup()
    t.goto(0, -n)
    t.pendown()
    t.circle(n)

for i in range(20,100,20):
    DrawCctCircle(i)

t.hideturtle()
t.done()
