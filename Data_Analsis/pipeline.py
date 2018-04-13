from sklearn.datasets import samples_generator
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import Pipeline

# 生成样本数据
x, y = samples_generator.make_classification(n_informative=4, n_features=20, n_redundant=0, random_state=5)
# 特征选择器
select_k_best = SelectKBest(f_regression, k=10)
# 随机森林分类器
classifier = RandomForestClassifier(n_estimators=50, max_depth=4)
# 构建机器学习流水线
pipeline_classifier = Pipeline([('selector', select_k_best), ('rf', classifier)])
pipeline_classifier.set_params(selector__k=6, rf__n_estimators=25)
# 训练分类器
pipeline_classifier.fit(x, y)

# 预测输出结果
prediction = pipeline_classifier.predict(x)
print('Predictions:', prediction)

# 打印分类器得分
print('Score:', pipeline_classifier.score(x, y))

# 打印被分类器选中的特征
features_status = pipeline_classifier.named_steps['selector'].get_support()
selected_features = []
for count, item in enumerate(features_status):
    if item:
        selected_features.append(count)

print('Selected features (0-indexed):', ','.join([str(x) for x in selected_features]))
