'''
@Author : sean cheng
@Email  : aya234@163.com
@CreateTime   : 2018/10/18
@program: 请用随机函数产生500行1-100之间的随机整数存入文件random.txt中，编程寻找这些整数的众数并输出，众数即为一组数中出现最多的数。
'''
import random

randNum = []

for _ in range(500):
    # 生成500个随机数
    randNum.append(str(random.randint(0,101)))

with open('random.txt','w+',encoding='utf-8') as txt:
    txt.write('\n'.join(randNum))
    txt.seek(0)  # 指针回到开始位置
    # 根据题意，是要先写入到文件，再从文件里面读出来，练习指针的操作。
    readNum=txt.read().split('\n')  # 按照回车符的划分，就可以得到列表

result = {}
for item in readNum:
    result[item] = result.get(item,0)+1

tmp = 0
keyNum = ''
for key, num in result.items():
    if num > tmp:
        tmp = num
        keyNum = key
print('众数是：',keyNum,'出现次数：',tmp)
