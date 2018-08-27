"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/21
@Program      : 回归，包括了线性回归、岭回归和多项式回归。
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import sklearn.metrics as ms


filename = 'data_singlevar.txt'
x = []
y = []

with open(filename, 'r') as f:
    for line in f.readlines():
        xt, yt = [float(i) for i in line.split(',')]
        x.append(xt)
        y.append(yt)

num_training = int(0.8 * len(x))
num_test = len(x) - num_training

x_train = np.array(x[:num_training]).reshape((num_training, 1))
y_train = np.array(y[:num_training])

x_test = np.array(x[num_training:]).reshape(num_test, 1)
y_test = np.array(y[num_training:])

linear_regressor = linear_model.LinearRegression()

linear_regressor.fit(x_train, y_train)  # 训练数据

y_train_pred = linear_regressor.predict(x_train)  # 预测数据
# plt.figure()
# plt.scatter(x_train, y_train, color='green')
# plt.plot(x_train, y_train_pred, color='black', linewidth=4)
# plt.show()

y_test_pred = linear_regressor.predict(x_test)
# plt.figure()
# plt.scatter(x_test, y_test, color='red')
# plt.plot(x_test, y_test_pred, color='blue', linewidth=4)
# plt.show()

print('训练集结果的均方误差', ms.mean_squared_error(y_train, y_train_pred))  # 这个值越小越好
print('训练集结果的解释方差分', ms.explained_variance_score(y_train, y_train_pred))  # 这个值越高越好
print('测试集结果的R方得分', ms.r2_score(y_train, y_train_pred))

print('-'*50)

print('测试集结果的均方误差', ms.mean_squared_error(y_test, y_test_pred))  # 这个值越小越好
print('测试集结果的解释方差分', ms.explained_variance_score(y_test, y_test_pred))  # 这个值越高越好
print('测试集结果的R方得分', ms.r2_score(y_test, y_test_pred))
"""是否训练集的数量越高，会不会解释方差分越高，同时均方误差越低，需要验证。"""

ridge_regressor = linear_model.Ridge(alpha=0.01, fit_intercept=True, max_iter=10000)
ridge_regressor.fit(x_train,y_train)
y_test_pred_ridge = ridge_regressor.predict(x_test)
print('-'*50)
print('(岭回归)测试集结果的均方误差', ms.mean_squared_error(y_test, y_test_pred_ridge))  # 这个值越小越好
print('(岭回归)测试集结果的解释方差分', ms.explained_variance_score(y_test, y_test_pred_ridge))  # 这个值越高越好
print('(岭回归)测试集结果的R方得分', ms.r2_score(y_test, y_test_pred_ridge))

polynomial = PolynomialFeatures(degree=3)
x_train_trainsformed = polynomial.fit_transform(x_train)
datapoint = [0.39, 2.78, 7.11]
poly_datapoint = polynomial.fit_transform(datapoint)

poly_linear_model = linear_model.LinearRegression()
poly_linear_model.fit(x_train_trainsformed, y_train)
print('_'*50)
print('线性回归：', linear_regressor.predict(datapoint)[0])
print('多项式回归：', poly_linear_model.predict(poly_datapoint)[0])