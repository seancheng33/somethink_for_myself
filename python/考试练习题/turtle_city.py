'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/9/6 
@Program       : 使用 turtle 库绘制简单城市剪影图形
'''

import turtle
turtle.setup(800,300)
turtle.penup()
turtle.fd(-350)
turtle.pendown()
def DrawLine(size):
    for angle in [0,90,-90,-90,90]:
        turtle.left(angle)
        turtle.fd(size)
for i in [20,30,40,50,40,30,20]:
    DrawLine(i)
turtle.hideturtle()
turtle.done()
