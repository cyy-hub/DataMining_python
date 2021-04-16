# 20210410 python 数据结构补充

# list.insert(i, x) 在下标为i的元素的前一个位置插入一个元素
# list.insert(0, x) 相当于list.append(x)  python 3 中已经改变该定义
list1 = [2, 3, 5]
list1.insert(0, 7)
print(list1)            # 输出：[7, 2, 3, 5]

# list 实现堆栈先进后出的结构：append(),pop()
# list 实现队列先进先出的就够：append(),pop(0),效率不高，推荐使用collection.deque
from collections import deque
queue = deque([7, 8, 9])
queue.append(10)
queue.append(11)
queue.popleft()
print(queue)            # 输出：deque([8, 9, 10, 11])

# 字符串-不变性，不能通过索引对其做任何修改

# 跨行字符串用三引号定义，（且别python的多行注视）
# 行尾添加\去除换行符号
s1 = '''你好
明天'''
s2 = '''你好\
明天'''
print(s1)
print(s2)

# 字符串包含转义字符，用r表示不转义的字符
print('E:\note\Python')
print(r'E:\note\Python')

# 字符串常用方法
str1 = "Zootopia"
print(str1.find("to"))  # 返回第一个to的索引
str2 = "Z o o t o p i a"
print(str2.split(" "))  # 以" "分割原字符串，返回一个list,['Z', 'o', 'o', 't', 'o', 'p', 'i', 'a']
print("".join(str2.split(" ")))  # 将字符串，List,元组中的元素以指定的字符连接一起。
str3 = ">".join(str1)   # Z>o>o>t>o>p>i>a

# Unicode 更多了是一种编码规则
# 优点是：为现代和古代每一个字符提供了一个统一的序号
# 创建：在字符串前面加u
unicode_str = u'\u4f60\u597d'
print(unicode_str)     # 输出：你好

# 元组的最大特征就是可访问不可改，可作为字典的键值，因为键值必须是唯一的
# 字典的创建
items = [('height', 180), ("weigh", 124)]
D = dict(items)
D2 = {'height': 180,
      'weigh': 124
      }
# 字典的遍历
category = {'apple': 'fruit',
            'Zootopia': 'film',
            'football': 'sport'}
keys = category.keys()
# keys.sort()   #  python3 返回的不再是list而是dict_keys(['apple', 'Zootopia', 'football'])
# print(keys)
# keys.sort(reverse=True)
# print(keys)   #
# # 自定义偏序关心进行排序, 其实是list sort函数特性
# def comp(str1, str2):
#     if str1[0] < str2[0]:
#         return 1
#     else:
#         return 0
# keys.sort(comp)
for key in keys:
    print(category[key])

# 集合-不可变的无序集合,元素唯一，用大括号定义，支持集合的交和并操作
set1 = {1, 2, 3}
set2 = set([2, 3, 4])
print(set1 - set2)  # 集合求差,包含在x 但是不包含在y中的元素：{1}
print(set1 | set2)  # 集合求并：{1, 2, 3, 4}
print(set1 & set2)  # 集合求交：{2, 3}
print(set1 ^ set2)  # 集合求异或， 只被一个集合包含的元素 {1, 4}
print(set1 > set2)  # 包含关系，set1 真包含于set2,返回True ：False





