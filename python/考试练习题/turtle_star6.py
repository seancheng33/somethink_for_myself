'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/9/10
@Program      : 使用turtle库的turtle.fd()函数和turtle.seth()函数绘制嵌套六角形，
                六角形边长从1像素开始，第一条边从0度方向开始，
                边长按照3个像素递增
'''

import turtle
edge = 6
d = 0
k = 1
for j in range(10):
   for i in range(edge):
       turtle.fd(k)
       d += 360/60
       turtle.seth(d)
       k += 3
turtle.done()
