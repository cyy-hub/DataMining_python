import pandas as pd
import numpy as np

data = {"id" : ["Jack", "Sarah", "Mike"],
        "age" : [18, 35, 20],
        "cash" : [10.53, 500.7, 13.6]}
df = pd.DataFrame(data)                                     # 默认列名
print(df)
df2 = pd.DataFrame(data, index=["one", "two", "three"])     # 设定列名
print(df2)

s = pd.Series({"a" : 4, "b": 9, "c" : 16}, name="number")
print(s)

# 系列的访问
print("-"*10)
print(s[0], s[:3])      # 下标，切片
print(s["a"])           # 索引
print(np.sqrt(s))

# dataFrame 的增删查改
print(df["id"])                     # 查
df["rich"] = df["cash"] > 200.0     # 增
print(df)
del(df["rich"])                     # 删除
print(df)