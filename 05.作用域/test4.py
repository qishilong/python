def make_multiplier(n):
    def multiplier(x):
        return n * x

    return multiplier


triple = make_multiplier(3)
print(triple(5))  # 15
print(triple(10))  # 30

double = make_multiplier(2)
print(double(7))  # 14
