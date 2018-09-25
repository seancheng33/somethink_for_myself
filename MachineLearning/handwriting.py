'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/9/19
@Program  : kNN算法的练习实例一则,手写数字的识别
'''
import numpy as np
import os
import kNN

def img2vector(filename):
    returnVect  = np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect


def handwritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = np.zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat = img2vector('trainingDigits/' + fileNameStr)
    testFileList = os.listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(m):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/' + fileNameStr)
        classifierResult = kNN.classify0(vectorUnderTest, trainingMat,hwLabels,3)
        print('the classifier came back with:{0},the real answer is:{1}'.format(classifierResult,classNumStr))
        if (classifierResult != classNumStr):errorCount += 1.0
    print('the total number of errors is:{}'.format(errorCount))
    print('the total erroe rate is:{:.2f}'.format(errorCount/float(mTest)))


if __name__ == '__main__':
    # testVector = img2vector('testDigits/0_13.txt')
    # print(testVector[0,0:31])
    # print(testVector[0,32:63])
    handwritingClassTest()
