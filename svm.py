# noinspection PyUnresolvedReferences
import numpy as np
import matplotlib.pyplot as plt
# noinspection PyUnresolvedReferences
from scipy import stats
# 使用seaborn绘制默认值
import seaborn as sns; sns.set()

#随机来点数据
from sklearn.datasets.samples_generator import make_blobs
X, y = make_blobs(n_samples=50, centers=2,
                  random_state=0, cluster_std=0.60)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
plt.show()
