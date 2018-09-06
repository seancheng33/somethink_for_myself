'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/9/6 
@Program       : 使用 turtle 库绘制5种多边形
'''

from turtle import *
for i in range(5):
    penup()    #画笔抬起
    goto(-200+100*i,-50)
    pendown()
    circle(40,steps=3+i)    #画某个形状
done()
