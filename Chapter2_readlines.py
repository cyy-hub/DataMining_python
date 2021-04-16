data = []
data1 = []
fr = open("readline_test.txt")
for line in fr.readlines():
    line = line.strip()          # 去掉字符串开头或者结尾的空白符，包括换行符
    data_line = line.split(",")  # 使用","分割数据并返回一个列表
    data_line1 = list(map(int, line.split(",")))
    data.append(data_line)
    data1.append(data_line1)

print(data)
print(data1)
fr.close()