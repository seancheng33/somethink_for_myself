'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/30
@Program      : （考试练习题）有一个文件data.txt,将文件的数据内容提取出来，
                计算每个人的平均工资，将其转化为字典salary，
                按照key的递增序在屏幕上显示输出score的内容.
'''

salarys = {}
fi = open("data.txt",'r',encoding='utf-8')

for l in fi:
    sv = eval(l)
    v= []
    k = ''
    for it in sv:
        if it == 'sid':
            k = sv[it]
        else:
            v.append(sv[it])
    else:
        tmp = 0
        for i in v:
            tmp += i
        v.append(int(tmp/len(v)))
        salarys[k]=v
fi.close()

so = list(salarys.items())
so.sort(key = lambda x:x[0],reverse = False)
for l in so:
    print('{}:{}'.format(l[0],l[1]))
