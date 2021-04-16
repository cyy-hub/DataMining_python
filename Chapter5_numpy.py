import numpy as np

# 1.创建数组
arr1 = np.array([1, 2, 3])
arr2 = np.array([(1.3, 9, 2.0), (7, 6, 1)])
arr3 = np.zeros((2, 3))
arr4 = np.identity(3) # 三维度单位阵
arr5 = np.random.random(size=(2, 3))

# 2.数组属性
print(arr2.shape)   # 矩阵的形状 (2, 3)
print(arr2.ndim)    # 矩阵的秩 2
print(arr2.size)    # 矩阵所有元素个数 6
print(arr2.dtype.name) # 矩阵中元素的类型 float64

# 3.数组访问
print(arr2[:1,:1])   # [[1.3]]
for row in arr2:
    print(row)
for element in arr2.flat:
    print(element)

# 4.数组运算
arr9 = np.array([[2, 1], [1, 2]])
arr10 = np.array([[1, 2], [3, 4]])
# 逐元素的+，-，*，/，%，操作
print(arr9 - arr10)
print(arr9**2)
print(arr9 * 3)
print(arr9 * arr10)
print(np.dot(arr9, arr10))  # 矩阵乘法
# 矩阵转置，求逆，求和，求极大，求极小
print(arr9.T)
print(np.linalg.inv(arr9))
print(arr9.sum(), arr9.max(), arr9.min())  # 6 2 1

# 5.通用函数sin,cos,都是针对整个数组逐元素操作
print(np.exp(arr9))
print(np.sin(arr9))
print(np.sqrt(arr9))

# 6.数组的合并和分割
arr11 = np.vstack((arr9, arr10))  # 纵向合并
arr12 = np.hstack((arr9, arr10))  # 横向合并
print(np.vsplit(arr12, 2))        # 纵向切割
print(np.hsplit(arr12, 2))        # 横向切割



