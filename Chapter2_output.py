f = open("outpu.txt", "w")  # 没有文件的话会新建一个
data = [['1', '2'], ['3', '4']]
line1 = ','.join(data[0])
f.write(line1 + '\n')
line2 = ','.join(data[1])
f.write(line2 + '\n')

# print 把原本输出到shell 的内容改输到文件中
data = [[1, 2], [3, 4]]
for line in data:
    print(str(line[0]) + ',' + str(line[1]), file=f)