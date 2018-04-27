'''
@Author : sean cheng
@Email  : aya234@163.com
@CreateTime   : 2018/4/27
打印斐波那契数列
'''


def fbis(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result


def main():
    result = fbis(20)
    for i, num in enumerate(result):
        print('第', i, '个数是：', num)


if __name__ == '__main__':
    main()