'''
@Author : sean cheng
@Email  : aya234@163.com
@CreateTime   : 2018/10/17
@program: 从键盘输入整数n（1-9之间），对于1-100之间的整数删除包含n并且能被n整除的数，例如如果n为6，则要删掉包含6的如6，16这样的数及是6的倍数的如12和18这样的数，输出所有满足条件的数，要求每满10个数换行。
'''


num = int(input('请输入一个100以内的整数：'))

j=0
for i in range(100):
    if (i+1) % num == 0:
        continue
    elif str(num) in str(i+1):
        continue
    else:
        print((i+1),end='')
    j += 1
    if j == 10:
        print()
        j = 0
