'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 18/5/28
3D散点图
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig =plt.figure()
ax = Axes3D(fig)

n = 250
f = lambda minval, maxval, n:minval + (maxval - minval) * np.random.rand(n)
x_vals = f(15, 41, n)
y_vals = f(-10, 70, n)
z_vals = f(-52, -37, n)

ax.scatter(x_vals, y_vals, z_vals, c='k', marker='o')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()