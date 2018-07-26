'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/17
@Program      : （考试练习题）给定一个文档，然后按要求处理，只需要原文里面的内容，
                其他的内容不需要，去掉原文里面开头的数字章节序号，保存至新文件
'''

import re
dataToWrite = []
flag = False
with open('论语-网络版.txt', 'r', encoding='utf-8') as fileIn:
    for line in fileIn:
        if '【' in line:
            flag = False
        if '【原文】' in line:
            flag = True
            continue
        if flag:
            line = line.lstrip()
            line = line.rstrip()
            dataToWrite.append(line)
with open('论语-提取版.txt','w',encoding='utf-8') as fileOut:
    for line in dataToWrite:
        if len(line) < 1:
            continue
        num = re.findall(r'\d+·\d+',line)
        if len(num)> 0:
            line = line.strip(num[0])
        fileOut.write(line+'\n')
