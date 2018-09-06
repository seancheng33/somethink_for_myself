'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/9/6 
@Program       : 使用 turtle 库绘制正方形螺旋线
'''

import turtle
n = 10
for i in range(1,10,1):
    for j in [90,180,-90,0]:
        turtle.seth (j)
        turtle.fd(n)
        n += 5
