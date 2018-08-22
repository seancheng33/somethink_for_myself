'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/8/22 
@Program       : 苏格拉底是古希腊著名的思想家、哲学家、教育家、公民陪审员。苏格拉底的部分名言被翻译为中文，
				 其部分内容由 sgld.txt 给出。请参考代码模板，补充代码完成中文分词和统计“人”出现的次数。
'''

import jieba
with open("sgld.txt","r",encoding ="utf-8")as f:
    lssgld = f.readlines()
n = 0
for ls in lssgld:
    wordlist = jieba.lcut(ls)
    if '人' in wordlist:
        n += 1
    
print('人:{}次'.format(n))
