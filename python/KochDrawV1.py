"""
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/9/13
@Program       : 科赫雪花绘制
"""

import turtle as t

def koch(size,n):
    if n == 0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)


def main():
    t.setup(600,600)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pensize(2)
    level = 3
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.hideturtle()
    t.done()


main()
