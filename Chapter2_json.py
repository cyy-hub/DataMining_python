import json
x = {"height": 176,
     "weight": 60
     }
print("原x", x)
y = json.dumps(x)  # 转化为字符串
print("序列化x", y)
x = json.loads(y)
print("反序列化x", x)

f = open("json_test.json", 'w')
json.dump(x, f)
f.close()

f = open("json_test.json", 'r')
print("从文件读取到的json", json.load(f))