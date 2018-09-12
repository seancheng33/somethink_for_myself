'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/9/12
@Program      : (1)读入 dir_300.txt 文件的内容，处理每一行文件名信息。
				将文件名中的学号内容以列表形式保存，丢掉‘0’的字串；
				照片的顺序编号作为字典的关键字，学号列表作为字典的值。
				转换后，显示字典中的每行信息
				（2）将该字典中的学号提取出来，构造另一个字典，以学号作为字典的关键字，
				累计学号出现的次数，将累计值作为字典的值。
				（3）累计字典中关键字的个数，即为实际参加测试的学生人数；累加每个关键字对应的值，
				即为所有学号测试次数；与实际测试人数之比，即为人均被测次数。
				将实际参加测试人数和人均被测次数显示输出在屏幕上。
'''
picd = {}
numd = {}
fi = open("dir_50.txt",'r')
for l in fi:
    l=l.replace('\n','').split('_')
    # print(l[1])
    lkey = l[1].split('.')[0]
#.....在此处输入代码.....
    lv = eval(l[0])
    for i in reversed(lv):
        if i == '0':
            lv.remove(i)
    # print("{}:{}".format(lkey,','.join(lv)))
    picd[lkey] = lv

fi.close()
idd = {}
for key in picd:
    for num in picd[key]:
        idd[num] = idd.get(num,0)+1
    # print(num,idd[num])

s = 0
for key in idd:
#    .....在此处输入代码.....
    s += idd[key]
    # print("{}:{}".format(key, idd[key]))
count = len(idd)
print("实际参加测试的人数是：",count)
print("人均被测次数是：{:.1f}".format(s/count))



 
