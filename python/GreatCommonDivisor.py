'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/9/6
@Program      : 欧几里得算法--求两个数的最大公约数算法
'''

def GreatCommonDivisor(a,b):
    if a < b:
        a,b = b,a
    r = 1
    while r !=0:
        r = a % b
        a = b
        b = r
    return a

m = eval(input())
n = eval(input())
print(GreatCommonDivisor(m,n))
