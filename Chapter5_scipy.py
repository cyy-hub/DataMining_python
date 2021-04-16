from scipy import poly1d
import numpy as np
p = poly1d([3, 4, 5])       # p(x) = 3x^2 + 4x + 5
print(p)
print(p * p)                # p*p = 9x^4 + 24x^3 + 46x^2 + 40x + 25
print(p.integ(k=6))         # 求p(x)的不定积分，指定常数项为6
print(p.deriv())           # 求p(x)的一阶导数： 6x + 4
print(p([4, 5]))            # 求p(4),p(5)的结果

def addsubtract(a, b):
    # 结合scipy的函数实现向量操作
    if a > b:
        return a - b
    else:
        return a + b
vec_addsubtract = np.vectorize(addsubtract)
print(vec_addsubtract([0, 3, 6, 9], [1, 3, 5, 7]))
vec_poly1d = np.vectorize(p)
print(vec_poly1d([4, 5]))          # 输出结果和p([4, 5]) 是一致的
