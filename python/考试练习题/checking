'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/8/22 
@Program       : 使用字典和列表型变量完成某课程的考勤记录统计，某班有 74 名同学，
				 名单由考生目录下文件 Name.txt 给出，某课程第一次考勤数据由考生目录下文件 1.csv 给出。请求出第一次缺勤同学的名单。
'''

# 从1.csv文件中读取考勤数据
with open("1.csv","r",encoding = "utf-8") as fo:
    foR = fo.readlines()
ls = []
for line in foR:
    line = line.replace("\n","")
    ls.append(line.split(","))

# 从name.txt文件中读取所有同学的名单
with open("Name.txt","r",encoding = "utf-8") as foName:
    foNameR = foName.readlines()
lsAll = []
for line in foNameR:
    line = line.replace("\n","")
    lsAll.append(line)

#求出第一次缺勤同学的名单
for l in ls:
    if l[0] in lsAll:
        lsAll.remove(l[0])

print("第一次缺勤同学有：",end ="")
for i in lsAll:
    print(i,end=' ')
