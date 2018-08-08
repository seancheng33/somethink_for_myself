'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/8
@Program      : pyplot绘制正弦波,练习显示中文的内容两种办法
'''
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# 方法一
# matplotlib.rcParams['font.family'] = 'SimHei'
# matplotlib.rcParams['font.size'] = 14
#
# a = np.arange(0.0, 5.0, 0.02)
#
# plt.xlabel('横轴：时间')
# plt.ylabel('纵轴：振幅')
# plt.plot(a, np.cos(2*np.pi*a), 'r--')

# 方法二
a = np.arange(0.0, 5.0, 0.02)

plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=20)
plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=20)
plt.plot(a, np.cos(2*np.pi*a), 'r--')

plt.show()