'''
@Author : sean cheng
@Email  : aya234@163.com
@CreateTime   : 2018/10/23
@program: 文件article.txt中存放了一篇英文文章（请自行创建并添加测试文本），假设文章中的标点符号仅包括“,”、“.”、“!”、“?”和“…”，编程找出其中最长的单词并输出。
'''

with open('article.txt','r',encoding='utf-8') as f:
    filedata = f.read().split('\n')

wordLenght = 0
word = ''
for item in filedata:
    repl = (',', '.', '!', '?','…')
    tempList = item.split(' ')
    for i in tempList:
        for j in repl:
            i = i.replace(j,'')
        if len(i) > wordLenght:
            word = i
            wordLenght = len(i)

print('最长的单词是:{0},长度为{1}'.format(word,wordLenght))
