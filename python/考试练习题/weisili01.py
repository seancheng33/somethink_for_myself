'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/31
@Program      : 统计《寻梦》《命运》两书的字符统计，将两个文件的前100个字存到文件
'''
import jieba

names = ['寻梦','命运']
for name in names:
    latterCount = {}
    with open(name+'-网络版.txt','r',encoding='utf-8') as inf:
        worddata = inf.read()
        for i in worddata:
            if i in ('\n','　',' ','，','。','﹖','』','『','"','：','﹗','…'):
                continue
            latterCount[i] = latterCount.get(i,0) + 1
    with open(name+'-汉字统计.txt','w',encoding='utf-8') as outf:
        ls = list(latterCount.items())
        ls.sort(key=lambda x:x[1],reverse=True)
        for i in range(100):
            ls[i] = '{}:{}'.format(ls[i][0],ls[i][1])
        outf.write(','.join(ls[:100]))
    
