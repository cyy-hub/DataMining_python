# 20210406
import matplotlib.pylab as plt
import numpy as np

# 1.柱状图
plt.subplot(2,1,1)
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor="#9999ff", edgecolor="white")
plt.bar(X, -Y2, facecolor="#ff9999", edgecolor="white")

# 利用plt.text 指定文字出现的坐标和内容
for x, y in zip(X,Y1):
    plt.text(x+0.4, y+0.05, "%.2f" % y, ha="center", va="bottom")
# 限制坐标轴的范围
plt.ylim(-1.25, +1.25)

# 2.饼状图
plt.subplot(2,2,3)
n = 20
Z = np.random.uniform(0, 1, n)
plt.pie(Z)

# 3.第三部分
plt.subplot(2, 2, 4)
# 等差数列
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
Y_C, Y_S = np.cos(X), np.sin(X)

plt.plot(X, Y_C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, Y_S, color="red", linewidth=2.5, linestyle="-")

# plt.xlim-限定坐标轴的范围，plt.xticks-改变坐标轴上刻度的文字
plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r"$-\pi$", r"$-\pi/2$", r"$0$", r"$+\pi/2$", r"$\pi$"])
plt.ylim(Y_C.min()*1.1, Y_C.max()*1.1)
plt.yticks([-1, 0, 1],
           [r"$-1$", r"$0$", r"$+1$"])
#plt.show()
plt.savefig("test.png")
