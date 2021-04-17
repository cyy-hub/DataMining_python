# 20210417 sklearn linear regression demo
# boston house price prediction
# 找到一个超平面，使得数据距离这个平面的误差最小
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
print(boston.keys())
# 输出 ：dict_keys(['data', 'target', 'feature_names', 'DESCR', 'filename'])
# 'data' : 数据，'feature_names': 特征名称， 'DESCRibe'：数据说明文档, 'target':目标值
print(boston.feature_names)
# 输出：['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']
x = boston.data[:, np.newaxis, 5]  # 第5列特征 "RM", np.newaxis增加一个新的维度
y = boston.target
lm = LinearRegression()
lm.fit(x, y)
print("方程的确定性系数（R^2）:%.2f" % lm.score(x,y))  # score 预测系数R^2 最好是1,R^2 = 1-u/v
# 方程的确定性系数（R^2）:0.48

plt.scatter(x, y, color='green')
plt.plot(x, lm.predict(x), color='blue', linewidth=3)
plt.xlabel('Average Number of Room pre Dwelling (RM)')
plt.ylabel('Housing Price')
plt.title('2D Demo of Linear Regression')
plt.savefig('Linear_Regression_of_Boston_Housing_Price.png')
plt.close()
