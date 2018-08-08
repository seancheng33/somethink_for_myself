'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/8
@Program      : pyplot散点图
'''

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')
ax.set_title('Simple Scatter')
plt.show()
