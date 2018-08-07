'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/8/6 
@Program       : 这段简单的numpy的ndarray代码，在mac里面运行，貌似有为，但是在win下的测试是正常的。
'''

import numpy as np

# def npSum():
#     a = np.array([0, 1, 2, 3, 4])
#     b = np.array([9, 8, 7, 6, 5])
#
#     c = a ** 2 + b ** 3
#
#     return c
#
# print(npSum())


a = np.array([0, 1, 2, 3, 4])
b = np.array([9, 8, 7, 6, 5])

print(a.dtype)  # 元素类型
print(a.shape)  # ndarray对象的尺度，对于矩形，n行m列
print(a.size)  # ndarray对象的元素个数，相当于.shape中n*m的值
print(a.itemsize)  # ndarray对象中每个元素的大小，以字节为单位
print(a.ndim)  # 秩，即轴的数量或维度的数量

c = a ** 2 + b ** 3

print(c)