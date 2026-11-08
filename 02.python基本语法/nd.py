a = 10
b = 3.5
c = "Python"
d = True
e = None

# 1. 数据类型与 type 函数
# a = type(1) == int
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>
print(type(e))  # <class 'NoneType'>
print(type(a) == int)  # True

# 2. 变量类型转换
print(int(b))  # 3
print(float(a))  # 10.0
print(str(a) + c)  # 10Python
print(bool(0))  # False
print(bool(""))  # False
print(bool("hello"))  # True

# 3. 算术运算符
print(a + 5)  # 15
print(a / 4)  # 2.5
print(a // 4)  # 2
print(a % 4)  # 2
print(a**2)  # 100
print(c * 2)  # PythonPython

# 4. 字符串格式化（f-string）
name = "Alice"
age = 25
print(f"姓名: {name}, 年龄: {age}")  # 姓名: Alice，年龄: 25
print(f"明年{age + 1}岁")  # 明年 26 岁
print(f"{a} + {5} = {a + 5}")  # 10 + 5 = 15

# 5. 比较运算符与链式比较
print(a > 5)  # True
print(a == 10)  # True
print(5 < a < 20)  # True
print(c == "python")  # False
print("A" < "a")  # True

# 6. 逻辑运算符
print(True and False)  # False
print(True or False)  # True
print(not d)  # False
print(0 and 5)  # 0
print(3 or 5)  # 3
print("" and "hello")  # ""
print("hi" or "hello")  # hi
print(not None)  # True

# 7. 三元运算符
score = 85
result = "及格" if score >= 60 else "不及格"
print(result)  # 及格
level = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(level)  # B

# 8. 赋值运算符
x = 10
x += 5
print(x)  # 15
x -= 3
print(x)  # 12
x *= 2
print(x)  # 24
x /= 4
print(x)  # 6.0

s = "Hi"
s += " Python"
print(s)  # Hi Python
s *= 2
print(s)  # Hi PythonHi Python


# 1. while 循环 + if-else
n = 1
result = 0
while n <= 5:
    if n % 2 == 0:
        result += n
    else:
        result -= n
    n += 1
print(result)  # -3

# 2. continue 和 break
num = 1
while num <= 10:
    if num == 3:
        num += 1
        continue
    if num == 7:
        break
    print(num)  # 1 2 4 5 6
    num += 1

# 3. 循环 else 子句
i = 0
while i < 3:
    print(i)  # 0 1 2
    i += 1
print("end")  # end

# 4. 嵌套条件
x = 15
if x < 10:
    print("A")
elif x < 20:
    if x % 2 == 0:
        print("B")
    else:
        print("C")
else:
    print("D")  # C

# 5. 综合练习
a = 1
b = 0
while a <= 5:
    if a == 3:
        b += 10
    elif a % 2 == 0:
        b += a * 2
    else:
        b += a
    a += 1
print(b)  # 28


### 作业三：BMI 计算器

# 编写一个 BMI 计算器程序，要求如下：

# 1. **用户输入**：通过 `input()` 函数获取用户的身高（单位：米）和体重（单位：千克）。

# 2. **计算 BMI**：使用公式 `BMI = 体重(kg) / 身高(m)²` 计算 BMI 值。

# 3. **判断分类**：根据 BMI 值判断身体状况（参考中国成人标准）：
#    - BMI < 18.5：偏瘦
#    - 18.5 ≤ BMI < 24：正常
#    - 24 ≤ BMI < 28：超重
#    - BMI ≥ 28：肥胖

# 4. **输出结果**：使用 f-string 格式化输出用户的 BMI 值和分类结果。

# 5. **健康建议**：根据分类结果给出相应的健康建议，例如：
#    - 偏瘦：建议适当增加营养摄入，进行适量运动
#    - 正常：保持良好的生活习惯
#    - 超重/肥胖：建议控制饮食，增加运动量

# **示例输出**：
# ```
# 请输入您的身高（米）：1.75
# 请输入您的体重（千克）：70
# 您的 BMI 值为：22.86
# 身体状况：正常
# 建议：保持良好的生活习惯，继续保持！
# ```

# height = float(input("请输入您的身高（米）："))
# weight = float(input("请输入您的体重（千克）："))
# BMI = weight / (height**2)
# if BMI < 18.5:
#     print(
#         f"您的 BMI 值为：{BMI}\n 身体状况：偏瘦\n 建议：建议适当增加营养摄入，进行适量运动"
#     )
# elif 18.5 <= BMI < 24:
#     print(
#         f"您的 BMI 值为：{BMI}\n 身体状况：正常\n 建议：保持良好的生活习惯，继续保持！"
#     )
# elif 24 <= BMI < 28:
#     print(f"您的 BMI 值为：{BMI}\n 身体状况：超重\n 建议：建议控制饮食，增加运动量")
# else:
#     print(f"您的 BMI 值为：{BMI}\n 身体状况：肥胖\n 建议：建议控制饮食，")

# ### 作业四：素数筛选器

# **素数（质数）** 是指在大于 1 的自然数中，除了 1 和它本身以外不再有其他因数的数。例如：2、3、5、7、11 都是素数，而 4、6、8、9 则不是。

# 编写一个程序，要求如下：

# 1. **用户输入**：通过 `input()` 函数获取起始数字和结束数字。

# 2. **输入合法性检查**：
#    - 输入必须是正整数（大于 0 的整数）
#    - 结束数字必须大于起始数字
#    - 如果输入不合法，给出相应提示并要求重新输入

# 3. **素数判断**：使用循环判断该范围内每个数字是否为素数。

# 4. **输出结果**：打印该范围内的所有素数，并统计素数的个数。

# **示例输出**：
# ```
# 请输入起始数字：10
# 请输入结束数字：50
# 10 到 50 之间的素数有：
# 11 13 17 19 23 29 31 37 41 43 47
# 共计 11 个素数
# ```

while True:
    start = int(input("请输入起始数字："))
    if start <= 0:
        print("输入无效，请输入一个正整数！")
        continue
    break

while True:
    end = int(input("请输入结束数字："))
    if end <= 0:
        print("输入无效，请输入一个正整数！")
        continue
    if end <= start:
        print("输入无效，结束数字必须大于起始数字！")
        continue
    break

print(f"{start} 到 {end} 之间的素数有：")

num = start
prime_count = 0

while num <= end:
    if num >= 2:
        # 判断 num 是否为素数
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            if prime_count > 0:
                print(" ", end='')
            print(num, end='')
            prime_count += 1

    num += 1


print(f"\n共计 {prime_count} 个素数")
