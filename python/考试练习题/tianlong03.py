'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/31
@Program      : （考试练习题）1.《天龙八部》文本中出现的汉字和标点符号进行统计,
                2.对《天龙八部》文本中出现的中文词语进行统计
'''
import jieba

latterCount = {}
with open('天龙八部-网络版.txt','r',encoding='utf-8') as inf:
    worddata = inf.read()
    # print(worddata)
    for i in worddata:
        if i == '\n':
            continue
        if i == ' ':
            continue
        latterCount[i] = latterCount.get(i,0) + 1
        
with open('天龙八部-汉字统计.txt','w',encoding='utf-8') as outf:
    for item in latterCount.items():
        outf.write('{}:{},'.format(item[0],item[1]))
        
wordCount = {}
with open('天龙八部-网络版.txt','r',encoding='utf-8') as inf:
    worddata = jieba.lcut(inf.read())
    for i in worddata:
        if i == '\n':
            continue
        if i == ' ':
            continue
        wordCount[i] = wordCount.get(i,0) + 1
        
with open('天龙八部-词语统计.txt','w',encoding='utf-8') as outf:
    for item in wordCount.items():
        outf.write('{}:{},'.format(item[0],item[1]))
