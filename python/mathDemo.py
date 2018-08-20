'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/16
@Program      : 基础练习，计算二次方程的实数根程序
'''

import math
def main():
    print("This program finds the real solutions to a quadratic\n")
    a, b, c = eval(input('Please enter the coefficients(a,b,c):'))
    delta = b * b - 4 * a * c
    if delta >=0:
        discRoot = math.sqrt(delta)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        peint('\nThe solutions are:', root1, root2)
    if delta < 0:
        print('The equation has no real roots')

main()
