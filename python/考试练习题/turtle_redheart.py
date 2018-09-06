'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/7/26 
@Program       : turtle 绘制粉红色填充红色线的心
'''

from turtle import *
color('red', 'pink')
begin_fill()
left(135)
fd(100)
right(180)
circle(50, -180)
left(90)
circle(50, -180)
right(180)
fd(100)
end_fill()
hideturtle()
done()
