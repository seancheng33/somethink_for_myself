'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/31
@Program      : （考试练习题）1.《天龙八部》文本中出现的汉字和标点符号进行统计,
                2.对《天龙八部》文本中出现的中文词语进行统计
                整体代码量比书里面的要少
'''
import jieba

latterCount = {}
with open('天龙八部-网络版.txt','r',encoding='utf-8') as inf:
    worddata = inf.read()
    for i in worddata:
        if i in ('\n','　'):
            continue
        latterCount[i] = latterCount.get(i,0) + 1
with open('天龙八部-汉字统计.txt','w',encoding='utf-8') as outf:
    ls = []
    for item in latterCount.items():
        ls.append('{}:{}'.format(item[0],item[1]))
    outf.write(','.join(ls))

    
wordCount = {}
with open('天龙八部-网络版.txt','r',encoding='utf-8') as inf:
    worddata = jieba.lcut(inf.read())
    for i in worddata:
        if i in ('\n','　'):
            continue
        wordCount[i] = wordCount.get(i,0) + 1
with open('天龙八部-词语统计.txt','w',encoding='utf-8') as outf:
    ls = []
    for item in wordCount.items():
        ls.append('{}:{}'.format(item[0],item[1]))
    outf.write(','.join(ls))
