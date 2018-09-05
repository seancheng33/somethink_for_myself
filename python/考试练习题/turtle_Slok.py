'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/7/26 
@Program       : turtle库绘制类似斯洛克形状图案
'''
import turtle
def drawCircle():
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
    turtle.fd(40)
def drawRowCircle(n):
    for j  in range(n,1,-1):
        for i in range(j):
            drawCircle()        
        turtle.fd(-j*40-20)
        turtle.right(90)
        turtle.fd(40)
        turtle.left(90)
        turtle.fd(40)
    drawCircle()
drawRowCircle(5)
turtle.hideturtle()
turtle.done()
