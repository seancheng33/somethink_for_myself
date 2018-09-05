'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/9/5
@Program       : 从键盘输入一些字符，逐个把它们写到指定的文件，直到输入一个@为止。
'''
filename = input("请输入文件名：\n")
fp = open(filename+'.txt','w',encoding='utf-8')
ch = input("请输入字符串：\n")
while True:
    if '@' in ch:
        fp.write(ch.split('@')[0])
        break
    else:
        fp.write(ch + " ")
    ch = input("请输入字符串：\n")
fp.close()
