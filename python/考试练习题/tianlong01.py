'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/30
@Program      : （考试练习题）统计文件出现的汉字和标点符号的数量
'''

dataDict = {}

with open('天龙八部-网络版.txt','r',encoding='utf-8') as incomeFile:
    txt = incomeFile.read()

for i in txt:
    if i == '\n':
        continue
    if i == '　':
        continue
    if i in dataDict.keys():
        dataDict[i] += 1
    else:
        dataDict[i] = 1

with open('天龙八部-汉字统计.txt','w',encoding='utf-8') as outFile:
    for item in dataDict.items():
        outFile.write("{}:{},".format(item[0],item[1]))
