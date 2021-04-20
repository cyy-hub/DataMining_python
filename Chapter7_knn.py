# 20210420
# knn classification test
# color map, pcolormesh test

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data[:, :2]      # 为了方便画图，仅去了数据的前两个特征
y = iris.target
# print(iris.DESCR)
print(iris.feature_names)
cmap_light = ListedColormap(['#FFAAAA', '#AAAAAA', '#AAAAFF'])  # 将list转换成 matplotlib.colors map对象
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

clf = KNeighborsClassifier(n_neighbors=15, weights='uniform')
clf.fit(X, y)

# 画决策边界，用不同的颜色表示
x0_min, x0_max = X[:, 0].min() - 1, X[:, 0].max() + 1
x1_min, x1_max = X[:, 1].min() - 1, X[:, 0].max() + 1

x0, x1 = np.meshgrid(np.arange(x0_min, x0_max, 0.02), np.arange(x1_min, x1_max, 0.02))   # 网格点的坐标矩阵-x0:返回第一维度坐标,x1:返回第二维坐标
Z = clf.predict(np.c_[x0.ravel(), x1.ravel()]).reshape(x0.shape)  # 计算网格处样本点对应的类别

plt.figure()
plt.pcolormesh(x0, x1, Z, cmap=cmap_light)    # Z:[395, 280]--0,1,2
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)  # y :150 -0,1,2 # 制定对应的色彩序列
plt.xlim(x0.min(), x0.max())
plt.ylim(x1.min(), x1.max())
plt.title("3-Class classification (k = 15, weights = 'uniform')")
plt.savefig("knn_test.png")
plt.show()
