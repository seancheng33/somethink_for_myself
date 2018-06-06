'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/6/5 
@Program  : 系统聚类算法练习一则
'''

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs

plt.figure(figsize=(12, 12))

n_samples = 1500
random_state = 170
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

y_pred = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward').fit_predict(X)

plt.subplot(221)
plt.scatter(X[y_pred == 0][:, 0], X[y_pred == 0][:, 1], marker='x', color='b')
plt.scatter(X[y_pred == 1][:, 0], X[y_pred == 1][:, 1], marker='+', color='r')
plt.title("Incorrect Number of Blobs")

y_pred = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward').fit_predict(X)

plt.subplot(222)
plt.scatter(X[y_pred == 0][:, 0], X[y_pred == 0][:, 1], marker='x', color='b')
plt.scatter(X[y_pred == 1][:, 0], X[y_pred == 1][:, 1], marker='+', color='r')
plt.scatter(X[y_pred == 2][:, 0], X[y_pred == 2][:, 1], marker='1', color='m')
plt.title("Correct Number of Blobs")

X_varied, y_varied = make_blobs(n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5],random_state=random_state)

y_pred = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward').fit_predict(X_varied)

plt.subplot(223)
plt.scatter(X[y_pred == 0][:, 0], X[y_pred == 0][:, 1], marker='x', color='b')
plt.scatter(X[y_pred == 1][:, 0], X[y_pred == 1][:, 1], marker='+', color='r')
plt.scatter(X[y_pred == 2][:, 0], X[y_pred == 2][:, 1], marker='1', color='m')
plt.title("Unequal Variance")

X_filtered = np.vstack((X[y == 0][:500],X[y == 1][:100],X[y == 2][:10]))
y_pred = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward').fit_predict(X_filtered)

plt.subplot(224)
plt.scatter(X_filtered[y_pred == 0][:, 0], X_filtered[y_pred == 0][:, 1], marker='x', color='b')
plt.scatter(X_filtered[y_pred == 1][:, 0], X_filtered[y_pred == 1][:, 1], marker='+', color='r')
plt.scatter(X_filtered[y_pred == 2][:, 0], X_filtered[y_pred == 2][:, 1], marker='1', color='m')
plt.title("Unevenly Sized Blobs")

plt.show()