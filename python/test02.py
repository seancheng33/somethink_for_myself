'''
@Author : sean cheng
@Email  : aya234@163.com
@CreateTime   : 2018/10/18
@program: 请用随机函数产生500行1-100之间的随机整数存入文件random.txt中，编程寻找这些整数的众数并输出，众数即为一组数中出现最多的数。
'''
import random

randNum = []

for _ in range(500):
    randNum.append(str(random.randint(0,101)))

with open('random.txt','w',encoding='utf-8') as txt:
    txt.write('\n'.join(randNum))

result = {}
for item in randNum:
    result[item] = result.get(item,0)+1

tmp = 0
keyNum = ''
for key, num in result.items():
    if num > tmp:
        tmp = num
        keyNum = key
print('众数是：',keyNum,'出现次数：',tmp)
