'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/8
@Program      : pyplot绘制正弦波,练习显示内容的标题，注解等信息
'''
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


a = np.arange(0.0, 5.0, 0.02)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=15, color='green')
plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=15)
plt.title('正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)
# plt.text(2, 1, '$\mu=100$', fontsize=15)
plt.annotate('$\mu=100$',xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.1, width=2))

plt.axis([-1, 6, -2, 2])
plt.grid(True)
plt.show()