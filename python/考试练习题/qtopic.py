'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/30
@Program      : （考试练习题）附件文件question.txt中有若干道Python选择题目，
                第1行的第1个数据为题号，后续的4行是4个选项，接下来是第二道题。
                读取其中的内容，提取题干和四个选项的内容，
                利用jieba分词并统计出现频率最高的3个词，
                其中要删除以下的常用字和符号
                 的，:：可以是和中或一个以下“”了其时产生DBC(第一个字符是空格)
                作为该题目的主题标签，显示输出在屏幕上
                
'''

import jieba
def qtopic(con):
    conls = jieba.lcut(con)
    dict = {}
    for word in conls:
        dict[word] = dict.get(word,0) + 1

    dictls = list(dict.items())
    dictls.sort(key=lambda x: x[1], reverse=True)
    k = 0
    for it in dictls:
        if it[0] in ' 的，:：可以是和中或一个以下“”了其时产生DBC':
            continue
        else:
            if k == 3:
                break
            else:
                print('{}:{}'.format(it[0], it[1]))
                k += 1


fi = open("question.txt", 'r',encoding='utf-8')
con = ''
num1 = 0
flag = 0
for l in fi:
    l = l.replace('\n', '').strip().split('.')
    # print(l)
    try:
        ft = eval(l[0])
    except:
        pass
    else:
        flag += 1
        num2 = num1
        num1 = ft
        if flag > 1:
            print('第{}题的主题是：'.format(num2))
            qtopic(con)
            con = ''
    con += l[1]
print('第{}题的主题是：'.format(num1))
qtopic(con)
fi.close()
