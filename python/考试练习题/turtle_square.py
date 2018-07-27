'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/7/26 
@Program       : turtle 绘制正方形螺旋线
'''

import turtle

n = 10
for i in range(1, 10, 1):
    for j in [90, 180, -90, 0]:
        turtle.seth(j)
        turtle.fd(n)
        n += 5

turtle.done()