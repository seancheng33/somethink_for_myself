'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/9/25
@Program  : 决策树算法的练习实例一则
'''
from math import log
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for fearVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelsCounts[currentLabel] = 0
        labelsCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt
