'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/8
@Program      : 
'''
import matplotlib.pyplot as plt
import numpy as np

# plt.plot([3, 1, 4, 5, 2])
# plt.ylabel("grade")
# plt.show()

a = np.arange(10)
plt.plot(a, a*1.5, 'go-', a, a*2.5, 'rx', a, a*3.5, '*', a, a*4.5, 'b-.')
plt.show()