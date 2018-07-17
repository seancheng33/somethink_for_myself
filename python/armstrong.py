'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/17
@Program      : 找出指定范围的阿姆斯特朗数
'''


def number(start, end):
    for num in range(start, end+1):
        digt = str(num)
        n = len(str(num))

        tmpNum = 0
        for i in range(n):
            tmpNum += int(digt[i]) ** n

        if tmpNum == num:
            print(num)


if __name__ == '__main__':
    number(1, 10000)
