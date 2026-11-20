x = 1


def func_a():
    x = 2

    def func_b():
        print(x)  # 2

    func_b()
    print(x)  # 2


func_a()
print(x)  # 1
