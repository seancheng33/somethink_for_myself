'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/17
@Program      : （考试练习题）去掉每行文字中所有的括号以及内部数字。
'''

import re
dataToWrite = []
flag = False
with open('论语-提取版.txt', 'r', encoding='utf-8') as fileIn:
    for line in fileIn:
        tmpline = ''
        for s in line:
            if s == '(':
                continue
            if s == ')':
                continue
            if s.isdigit():
                continue
            tmpline += s
        dataToWrite.append(tmpline)
            
with open('论语-原文.txt','w',encoding='utf-8') as fileOut:
    for line in dataToWrite:
        fileOut.write(line+'\n')
