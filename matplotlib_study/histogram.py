'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 18/5/29
直方图
'''

import numpy as np
import matplotlib.pyplot as plt

apples = [30, 25, 22, 36, 21, 29]
oranges = [24, 33, 19, 27, 35, 20]

num_groups = len(apples)
fig, ax = plt.subplots()

indices = np.arange(num_groups)

bar_width = 0.2
opacity = 0.6

hist_apples = plt.bar(indices, apples, bar_width, alpha=opacity, color='g', label='Apples')
hist_oranges = plt.bar(indices+bar_width, oranges, bar_width, alpha=opacity, color='b', label='Oranges')

plt.xlabel('Month')
plt.ylabel('Production quantity')
plt.title('Comparing apples and oranges')
plt.xticks(indices+bar_width/2, ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'))
plt.ylim([0, 45])
plt.legend()
plt.tight_layout()

plt.show()