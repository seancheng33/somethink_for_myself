"""
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/8/17 
@Program       : 基础练习，用来计算pi的
"""

from random import random
from math import sqrt
from time import clock

DARTS = 2**30
hits = 0
clock()
for i in range(1,DARTS):
	x, y = random(),random()
	dist = sqrt(x**2+y**2)
	if dist <= 1.0:
		hits = hits + 1
pi = 4 * (hits/DARTS)
print('Pi的值是{}'.format(pi))
print('程序运行时间是 %-5.5ss' % clock())