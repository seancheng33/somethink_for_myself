'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/30
@Program      : （考试练习题）统计文件出现的词语和标点符号的数量
'''
import jieba

dataDict = {}

with open('天龙八部-网络版.txt','r',encoding='utf-8') as incomeFile:
    txt = incomeFile.read()

words = jieba.cut(txt)
for i in words:
    if i == '\n':
        continue
    if i == '　':
        continue
    if i in dataDict.keys():
        dataDict[i] += 1
    else:
        dataDict[i] = 1

with open('天龙八部-词语统计.txt','w',encoding='utf-8') as outFile:
    tmpList = []
    for item in dataDict.items():
        tmpList.append("{}:{}".format(item[0],item[1]))
    outFile.write(','.join(tmpList))
