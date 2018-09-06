'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/9/6 
@Program       : turtle 绘制红色的五角星
'''

from turtle import *
setup(400,400)
penup()
goto(-100,50)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(200)
    right(144)
end_fill()
hideturtle()
done()
