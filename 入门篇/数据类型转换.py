num_str = str(11)

print(type(num_str), num_str)

float_str = str(1.1245)

print(type(float_str), float_str)

str_num = int("12345")
print(type(str_num), str_num)

float_num = float("3.14159")
print(type(float_num), float_num)

# 错误示例，想要将字符串转换为数字，需要保证字符串里面的内容都是数字
# anyStr_num = int("nihao")
# print(
#     type(anyStr_num), anyStr_num
# )  # This will raise a ValueError because "nihao" cannot be converted to an integer

# 整数转浮点数
int_to_float = float(100)
print(type(int_to_float), int_to_float)

# 浮点转整数（会丢失精度，只保留整数部分）
float_to_int = int(9.99)
print(type(float_to_int), float_to_int)

# 字符串转整数，失败，因为字符串表示的是浮点数
# str_to_num = int("88.88")
# print(type(str_to_num), str_to_num)

# 字符串转浮点数，成功
str_to_float = float("88.88")
print(type(str_to_float), str_to_float)

val = {"100", "3.14", "hello", "200"}
val_str = str(val)
print(val, type(val_str), val_str)
