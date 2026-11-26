# a = 1
# print(a)

# del a
# print(a)


# class Animal:
#     def __init__(self, name):
#         self.name = name


# dog = Animal("dog")

# print(vars(dog))
# print(vars())
# print(locals())
# print(vars)


class Dog:
    def __init__(self, name):
        self.name = name


dog = Dog("Buddy")

# 添加一个属性
dog.age = 3
print(dog.age)  # 3

# 删除属性
delattr(dog, "age")
# print(dog.age)          # AttributeError!

# 等价于
# del dog.age
