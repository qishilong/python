# map 映射 对可迭代对象的每个元素执行指定操作，返回结果的迭代器。


numbers = [1, 2, 3, 4, 5]


# 普通写法
# def square(x):
#     return x**2


# result = map(square, numbers)
# print(list(result))

# lambda 表达式写法
# result = map(lambda x: x**2, numbers)
# print(list(result))


# filter 过滤 根据条件筛选可迭代对象中的元素，保留满足条件的。
# 筛选偶数
# result = filter(lambda x: x % 2 == 0, numbers)
# print(list(result))

# 筛选正数
# nums = [-1, -2, 1, 2, 5]
# result_nums = filter(lambda x: x > 0, nums)
# print(list(result_nums))


# sorted 排序排序（指定key）
# sorted() 和列表的 .sort() 都支持 key 参数，用于指定"按什么排序"。
# words = ["banana", "pie", "Washington", "book"]

# # 按长度排序
# result = sorted(words, key=lambda x: len(x))
# print(result)

# # 按最后一个字母排序
# result_last = sorted(words, key=lambda x: x[-1])
# print(result_last)

# # 按长度倒序排序
# result_reverse = sorted(words, key=lambda x: len(x), reverse=True)
# print(result_reverse)


# max() / min() — 极值（指定key）
# words = ["apple", "banana", "cherry"]

# # 找出最长的单词
# result_max = max(words, key=lambda x: len(x))
# print(result_max)

# # 找出最短的单词
# result_min = min(words, key=lambda x: len(x))
# print(result_min)

# students = [
#     {"name": "Alice", "score": 85},
#     {"name": "Bob", "score": 92},
#     {"name": "Charlie", "score": 78},
# ]

# # 找出分数最高的学生
# result_max_score = max(students, key=lambda x: x["score"])
# print(result_max_score)


# reduce() — 累积计算
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 求和
result_sum = reduce(lambda x, y: x + y, numbers)
print(result_sum)

# 求积
result_product = reduce(lambda x, y: x * y, numbers)
print(result_product)

# 求最大值
result_max = reduce(lambda x, y: max(y, x), numbers)
print(result_max)
