'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/7
@Program      : 图片处理,将图片转换为数组，然后处理数组，然后重新保存为图片
'''

from PIL import Image
import numpy as np

a = np.array(Image.open("right.jpg"))
# print(a.shape, a.dtype)
b = [255, 255, 255] - a
im = Image.fromarray(b.astype('uint8'))
im.save('fixed2.png')