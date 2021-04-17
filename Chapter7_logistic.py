# 20210417 sklear logistic regression
# h(x) = 1/(1+exp(-w^Tx))
# 依据数据确定一组合适的参数，在对原始样本进行加权求和后，通过激活函数做非线性变换，得到表示该样本属于正类的概率
# w 的学习牛顿法，梯度下降法
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('../data/LogisticRegression.csv')   # 数据是没有准备,下载了最后没法解压
# get_dummies 是利用pandas实现one hot encode的方式
data_dum = pd.get_dummies(data, prefix='rank', colums=['rank'], drop_first=True)

print(data_dum.head(5))

X_train, X_test, y_train, y_test = train_test_split(data_dum.ix[:, 1], data_dum.ix[:, 0], test_size=0.1, random_state=520)
lr = LogisticRegression()
lr.fit(X_train, y_train)
print('罗辑回归的准确率：{0:.2f}%'.format(lr.score(X_test, y_test) * 100))

