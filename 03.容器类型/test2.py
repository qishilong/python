t = (5, 2, 8, 2)
first, *rest = t
print(first, rest)  # 5, [2, 8, 2]
print(sorted(t))  # [2,2,5,8]
print(2 in t, 9 not in t)  # True, True

s = set(t)
print(len(s))  # 3
print(
    s
)  # {8,2,5} 输出顺序不固定，由解释器决定，Set是无序的，需要固定顺序时，要显示排序。sorted(s)
s2 = {2, 8, 10}
print(s & s2, s | s2)  # {2,8} {2,5,8,10}
