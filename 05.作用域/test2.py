count = 0


def outer():
    count = 10

    def inner():
        global count
        count += 1
        print(count)  # 1

    inner()
    print(count)  # 10


outer()
print(count)  # 1
