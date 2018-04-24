'''
@author: Sean Cheng
算法练习：二分查找算法
利用一个猜100以内的数字实现
'''
import random


def main():
    num = random.randint(0, 100)  # 生成一个0-99之间的随机数
    num_array = [i for i in range(100)]  # 生成一个0-99的数组
    index_high = len(num_array)  # 上界标为数组的长度
    index_low = 0  # 下界标为数组的第一个数
    index_mid = (index_high + index_low) // 2  # 中间点

    while True:
        # 无限循环，直到找到上面生成的随机数
        if num_array[index_mid] > num:
            # 中间点的数组如果比随机数大，上界标改为中间点减一，重新定义中间点
            print('猜', num_array[index_mid])
            index_high = index_mid - 1
            index_mid = (index_high + index_low) // 2
        elif num_array[index_mid] < num:
            # 中间点的数组如果比随机数大，下界标改为中间点加一，重新定义中间点
            print('猜', num_array[index_mid])
            index_low = index_mid + 1
            index_mid = (index_high + index_low) // 2
        elif num_array[index_mid] == num:
            print('猜', num_array[index_mid])
            print('答案', num)
            break


if __name__ == '__main__':
    main()
