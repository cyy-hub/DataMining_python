# 20210413 类代码实例

class Pokemon(object):
    def __init__(self, name, gender, level, type, status):
        self.__type = type
        self.__gender = gender
        self.__name = name
        self.__level = level
        self.__status = status
        self.__info = [self.__name, self.__type, self.__gender, self.__level, self.__status]
        self.__index = -1

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    def getType(self):
        return self.__type

    def getStatus(self):
        return self.__status

    def lever_up(self):
        self.__status = [s+1 for s in self.__status]
        self.__status[0] += 1    # 依据具体的升级规则确定

    def __iter__(self):
        # 返回一个拥有next方法的对象
        # 可以实现在容器中逐一访问元素
        print('名字 属性 性别 级别 等级 能力')
        return self

    # def next(self):      # python 2.0的写法
    def __next__(self):    # python 3.0的写法
        if self.__index == len(self.__info)-1:
            raise StopIteration
        else:
            self.__index += 1
            return self.__info[self.__index]

class Charmander(Pokemon):
    def __init__(self, name, gender, level):
        self.__type = ('fire', None)
        self.__gender = gender
        self.__name = name
        self.__level = level
        self.__status = [10+2*level, 5+1*level, 5+1*level, 5+1*level, 5+1*level, 5+1*level]
        Pokemon.__init__(self, self.__name, self.__gender, self.__level, self.__type, self.__status)

pokemon1 = Charmander("Bang", 'male', 5)
print(pokemon1.getGender())

# 为私有化
# print(pokemon1.__type)    # 报错：'Charmander' object has no attribute '__type'
print(pokemon1._Charmander__type)

pokemon2 = Pokemon("abc", "male", 5, 'fire', 0)
for info in pokemon2:
    print(info)

# for 循环的迭代机制：在容器对象上调用了iter()方法，
# iter 方法返回一个对象，该对象封装了next()方法，用于遍历封装内容
# for info in pokemon1():
#     print(info)

"""    for info in pokemon1():
TypeError: 'Charmander' object is not callable
难道是因为没有重写么？
"""

print(dir(pokemon1))
print(dir(pokemon2))