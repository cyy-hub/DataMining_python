def sum_numbers(num1, *numbers):
    print(num1, numbers)        # 1 (2, 3, 4)
    s = num1
    for val in numbers:
        s += val
    print(s)                    # s = 10

sum_numbers(1,2,3,4)


# 可变对象
def changeable(list):
    list[0] = 2
    print(list)
lis = [1, 2, 3]
print(lis)
changeable(lis)
print(lis)

# globals()函数
x = 1
def print_x():
    x = 2
    print(globals()["x"])
    print(x)
print_x()

# 声明全局变量
def defin_gx():
    global gx
    gx = 3
gx = 1
defin_gx()
print(gx)

# lambda表达式
g = lambda x : x + 1
print(g(1))

from math import log


def make_logarithmic_function(base):
    return lambda x:log(x, base)
my_lf = make_logarithmic_function(base=3)

print(my_lf(9))


