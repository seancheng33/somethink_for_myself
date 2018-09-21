'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/9/19
@Program  : kNN算法的练习实例一则,手写数字的识别
'''
import numpy as np

def img2vector(filename):
    returnVect  = np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect


if __name__ == '__main__':
    testVector = img2vector('testDigits/0_13.txt')
    print(testVector[0,0:31])
    print(testVector[0,32:63])
