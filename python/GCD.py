'''
@Author : sean cheng
@Email  : aya234@163.com
@CreateTime   : 2018/9/29
@program: 欧几里得算法求解最大公因数,使用递归的形式实现
'''

def GCD(a,b):
    if b == 0:
        return a
    a, b = b, a%b
    return GCD(a,b)
if __name__ in '__main__':
    print(GCD(2009,1394))
