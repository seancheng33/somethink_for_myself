'''
按照书上面的内容的练习
这是一个简单的销售预测，
'''
import re
import numpy
from sklearn import linear_model
from matplotlib import pyplot as plt

# 读取数据
with open('data.txt', 'r') as fn:
    all_data = fn.readlines()

# 数据清洗，按照数据源的格式，将数据分别添加到两个list中
x = []
y = []
for single_data in all_data:
    tmp_data = re.split('\t|\n', single_data) # 用正则表达式来分割数据
    x.append(float(tmp_data[0]))
    y.append(float(tmp_data[1]))

# 列表类型转换为数组类型，数组形状为100行、1列
x = numpy.array(x).reshape([100, 1])
y = numpy.array(y).reshape([100, 1])

# matplotlib的散点图展示
plt.scatter(x, y)
# plt.show()

# sklearn的线性回归建模
model = linear_model.LinearRegression()
model.fit(x, y)

# 模型评估
model_coef = model.coef_
model_intercept = model.intercept_
r2 = model.score(x, y)

# print(r2)

# 新数据的预测
new_x = 84610
pre_y = model.predict(new_x)

# print(pre_y)
