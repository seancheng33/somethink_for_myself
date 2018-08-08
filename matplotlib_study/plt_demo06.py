'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/8
@Program      : pyplot绘制直方图
'''

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
mu, sigma = 100, 20
a = np.random.normal(mu, sigma, size=100)

plt.hist(a, 20, normed=1, histtype='stepfilled', facecolor='b', alpha=0.75)
plt.title('Histogram')

plt.show()
