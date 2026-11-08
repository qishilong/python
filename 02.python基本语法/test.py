print(6)
print(0b1010)
print(True)
print("""Hello 
World
""")

print('''Hello
world''')  # 多行字符串


print(None)


print("""


""")

# type 函数
print(type(100))
print(type(0b1010))
print(type(100) == int)
print(type(None))

# python 中所有数据均是对象


# 变量
## Python是动态类型语言，变量无需声明类型，直接赋值即可创建。
a, b, c = 1, 2, 3

x, y = 10, 20

print(x, y)

x, y = y, x

print(x, y)


print(bool(None))
print(type(type(bool(type(1)))))
print(type("<class 'type'>"))


# # 海象运算符
# while (line := input("输入: ")) != 'quit':
#     print(f"你输入了：{line}")


# while else 语句
num = 1
while num <= 9:
    if num == 4:
        print('找到：4')
        break
    num += 2
else:
    print('没有找到：4')


# 三元运算符
a = 1
result = "a大于0" if a > 0 else "a小于等于0"
print(result)

# 嵌套三元运算符
b, c = -1, 0
result_b = "b大于0" if b > 0 else (b == 0 and "b等于0" or "b小于0")
result_c = "c大于0" if c > 0 else (c == 0 and "c等于0" or "c小于0")
print(result_b)
print(result_c)
