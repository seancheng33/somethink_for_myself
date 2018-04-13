import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

# 输入数据
x = np.array([[1, 1], [1, 3], [2, 2], [2.5, 5], [3, 1], [4, 2], [2, 3.5], [3, 3], [3.5, 4]])
# 寻找最近邻的数量
num_neighbors = 3
# 输入数据点
input_point = [[2.6, 1.7]]

# 画出数据点
plt.figure()
plt.scatter(x[:, 0], x[:, 1], marker='o', s=25, color='k')

# 建立最近邻模型
knn = NearestNeighbors(n_neighbors=num_neighbors, algorithm='ball_tree').fit(x)
distances, indices = knn.kneighbors(input_point)

# 打印k个最近邻点
print('k nearest neighbors')
for rank, index in enumerate(indices[0][:num_neighbors]):
    print(str(rank * 1) + '--->', x[index])

# 画出最邻近点
plt.figure()
plt.scatter(x[:, 0], x[:, 1], marker='o', s=25, color='k')
plt.scatter(x[indices][0][:][:, 0], x[indices][0][:, 1], marker='o', s=150, color='k',facecolors='none')
plt.scatter(input_point[0],input_point[1],marker='x',s=150,color='k')
plt.show()
