'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/8/7
@Program      : 随机读取指定文件里面的人名
'''
import random

ls=[]
with open('name.txt','r') as f:
    for item in f.readlines():
        ls.append(item.replace('\n',''))

print(random.choice(ls))

