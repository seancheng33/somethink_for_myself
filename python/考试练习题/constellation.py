'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/30
@Program      : （考试练习题）读取csv文件中的数据，循环获的用户输入，直至用户
                输入回车退出。根据用户输入的星座名称，输出此星座的出生日期范围
                及对应字符形式，如果输入有误，输出“输入的星座名称有误”
'''
dataline = []

with open('SunSign.csv','r') as csvfile:
    for line in csvfile:
        dataline.append(line.replace('\n','').split(','))
print(dataline) 
while True:
    interStr = input('请输入星座中文名称（例如：双子座）：')

    if interStr == '':
        break;
    signlist = []
    for item in dataline[1:]:
        signlist.append(item[0])
        if interStr == item[0]:
            print(chr(int(item[-1]))+'座的生日位于'+item[1]+'-'+item[2]+'之间。')
		
    if interStr not in signlist:
        print('输入星座名称有误！')
        continue
