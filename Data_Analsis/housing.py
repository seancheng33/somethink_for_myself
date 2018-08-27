"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/27
@Program      : 决策树回归、AdaBoost算法
"""
from sklearn import datasets
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score
from sklearn.utils import shuffle

housing_data = datasets.load_boston()
x, y = shuffle(housing_data.data, housing_data.target, random_state=7)
num_training = int(0.8*len(x))
x_train, y_train = x[:num_training], y[:num_training]
x_test, y_test = x[num_training:], y[num_training:]

dt_regressor = DecisionTreeRegressor(max_depth=4)
dt_regressor.fit(x_train, y_train)

ab_regressor = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=400, random_state=7)
ab_regressor.fit(x_train, y_train)

y_pred_dt = dt_regressor.predict(x_test)
mes = mean_squared_error(y_test, y_pred_dt)
evs = explained_variance_score(y_test, y_pred_dt)
print('(决策树)测试集结果的均方误差', round(mes, 2))  # 这个值越小越好
print('(决策树)测试集结果的解释方差分', round(evs, 2))  # 这个值越高越好

y_pred_ab = ab_regressor.predict(x_test)
mes = mean_squared_error(y_test, y_pred_ab)
evs = explained_variance_score(y_test, y_pred_ab)
print('(AdaBoost算法)测试集结果的均方误差', round(mes, 2))  # 这个值越小越好
print('(AdaBoost算法)测试集结果的解释方差分', round(evs, 2))  # 这个值越高越好