# 变量定义
a = 10
b = 3.5
c = "Python"
d = True
e = None

# 1. 数据类型与 type 函数
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>
print(type(e))  # <class "NoneType'>
print(type(a) == int)

# 2. 变量类型转换
print(int(b))
print(float(a))
print(str(a) + c)
print(bool(0))
print(bool(""))
print(bool("hello"))

# 3. 算术运算符
print(a + 5)
print(a / 4)
print(a // 4)
print(a % 4)
print(a**2)
print(c * 2)

# 4. 字符串格式化（f-string）
name = "Alice"
age = 25
print(f"姓名: {name}, 年龄: {age}")
print(f"明年{age + 1}岁")
print(f"{a} + {5} = {a + 5}")

# 5. 比较运算符与链式比较
print(a > 5)
print(a == 10)
print(5 < a < 20)
print(c == "python")
print("A" < "a")

# 6. 逻辑运算符
print(True and False)
print(True or False)
print(not d)
print(0 and 5)
print(3 or 5)
print("" and "hello")
print("hi" or "hello")
print(not None)

# 7. 三元运算符
score = 85
result = "及格" if score >= 60 else "不及格"
print(result)
level = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(level)

# 8. 赋值运算符
x = 10
x += 5
print(x)
x -= 3
print(x)
x *= 2
print(x)
x /= 4
print(x)

s = "Hi"
s += " Python"
print(s)
s *= 2
print(s)
