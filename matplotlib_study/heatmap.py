'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 18/5/29 
热力图
'''
import numpy as np
import matplotlib.pyplot as plt

group1 = ['France', 'Italy', 'Spain', 'Portugal', 'Germany']
group2 = ['Japan', 'China', 'Brazil', 'Russia', 'Australia']

data = np.random.rand(5, 5)
fig, ax = plt.subplots()
heatmap = ax.pcolor(data, cmap=plt.cm.gray)

ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)

ax.invert_yaxis()
ax.xaxis.tick_top()

ax.set_xticklabels(group2, minor=False)
ax.set_yticklabels(group1, minor=False)

plt.show()
plt.save


