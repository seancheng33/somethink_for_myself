'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/7/26 
@Program       : turtle 绘制金色的八角星
'''

import turtle as t

t.colormode(255)
t.color(255, 215, 0)
t.begin_fill()
for x in range(8):
	t.fd(200)
	t.lt(225)
t.end_fill()
t.hideturtle()
t.done()