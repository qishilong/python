# 双引号定义法
name = "你好"

# 三引号定义法
name1 = """你好1"""
name2 = """
你好2
你好3
"""

print(type(name))
print(type(name1))
print(type(name2))

# 变成普通的符号"你好4"
name3 = '"你好4"'
print(name3)

# 变成普通的符号'你好5'
name4 = "'你好5'"
print(name4)

name5 = "hello"
nameStr = "你好" + name5  # 字符串拼接
print(nameStr)

name6 = 123456
# nameNumberStr = "number" + name6
# print(nameNumberStr)  # 这里会报错，因为不能直接拼接字符串和数字

"""字符串格式化"""
number1 = 1
number2 = 2
str = "number"
numberStr = "%s: %s + %s = %s" % (
    str,
    number1,
    number2,
    number1 + number2,
)  # 使用%格式化字符串
print(numberStr)

a = "hello"
b = 1
c = 2
str1 = "%s, %d, %f" % (a, b, c)  # 使用%格式化字符串
print(str1)
