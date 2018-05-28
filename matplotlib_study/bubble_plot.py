'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 18/5/28
气泡图
'''

import numpy as np
import matplotlib.pyplot as plt

num_vals = 40

x = np.random.rand(num_vals)
y = np.random.rand(num_vals)

max_radius = 25
area = np.pi * (max_radius * np.random.rand(num_vals)) ** 2

colors = np.random.rand(num_vals)

plt.scatter(x, y, s=area, c=colors, alpha=1.0)

plt.show()
