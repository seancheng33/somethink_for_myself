'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 18/5/29
饼图
'''
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Apple': 26,
    'Mango': 17,
    'Pineapple': 21,
    'Banana': 29,
    'Strawberry': 11}

colors = ['orange', 'lightgreen', 'lightblue', 'gold', 'cyan']  # 颜色设定

explode = (0.1, 0, 0, 0, 0)  # 设置是否有需要突出的部分

plt.pie(data.values(), explode=explode, labels=data.keys(), colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 设置图形是一个正圆

plt.show()