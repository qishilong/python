# 实现函数 `flatten`，接收一个可能包含嵌套列表的列表（如 `[1, [2, 3], [[4], 5]]`），返回一个将所有元素展开后的一维列表（如 `[1, 2, 3, 4, 5]`）。
# nested1 = [1, [2, 3], [[4], 5]]
# print(flatten(nested1))  # [1, 2, 3, 4, 5]

# nested2 = [[[1]], 2, [3, [4, [5]]]]
# print(flatten(nested2))  # [1, 2, 3, 4, 5]

# print(flatten([]))  # []
# print(flatten([1, 2, 3]))  # [1, 2, 3]


def flatten(nest_list):
    result = []
    for item in nest_list:
        if type(item) is list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


# nested1 = [1, [2, 3], [[4], 5]]
# print(flatten(nested1))  # [1, 2, 3, 4, 5]

# nested2 = [[[1]], 2, [3, [4, [5]]]]
# print(flatten(nested2))  # [1, 2, 3, 4, 5]

# print(flatten([]))  # []
# print(flatten([1, 2, 3]))  # [1, 2, 3]

# 实现函数 `to_linked_list`，接收一个列表或元组，将其转换为一个链表结构并返回。
# linked1 = to_linked_list((1, 2, 3))
# print(linked1)
# # {'value': 1, 'next': {'value': 2, 'next': {'value': 3, 'next': None}}}

# linked2 = to_linked_list([10, 20])
# print(linked2)
# # {'value': 10, 'next': {'value': 20, 'next': None}}

# print(to_linked_list([]))  # None


def to_linked_list(value: list | tuple | None):
    if not value:
        return None

    head = {'value': value[0], 'next': None}
    current = head
    for i in value[1:]:
        current['next'] = {'value': i, 'next': None}
        current = current['next']
    return head


# linked1 = to_linked_list((1, 2, 3))
# print(linked1)
# # {'value': 1, 'next': {'value': 2, 'next': {'value': 3, 'next': None}}}

# linked2 = to_linked_list([10, 20])
# print(linked2)
# # {'value': 10, 'next': {'value': 20, 'next': None}}

# print(to_linked_list([]))  # None

# print(not [])
# print(not [1])
# print(not None)
# print(not {})
# print(not ())

# 实现函数 `merge_dicts`，接收不定数量的字典参数，将它们合并为一个大字典。
# 合并规则：求并集，如果有相同的键，后传入的字典中的值覆盖先传入的字典中的值（浅合并即可）

# d1 = {"a": 1, "b": [1, 2]}
# d2 = {"b": [3], "c": "hello"}
# d3 = {"a": 10, "d": True}

# merged = merge_dicts(d1, d2, d3)
# print(merged)
# # {'a': 10, 'b': [3], 'c': 'hello', 'd': True}

# print(merge_dicts(d1))
# # {'a': 1, 'b': [1, 2]}

# print(merge_dicts())
# # {}


# def merge_dicts(*args):
#     result = {}
#     for d in args:
#         result.update(d)
#     return result\


def merge_dicts(*args):
    result = {}
    for d in args:
        for k, v in d.items():
            result[k] = v
    return result


d1 = {"a": 1, "b": [1, 2]}
d2 = {"b": [3], "c": "hello"}
d3 = {"a": 10, "d": True}

merged = merge_dicts(d1, d2, d3)
print(merged)
# {'a': 10, 'b': [3], 'c': 'hello', 'd': True}

print(merge_dicts(d1))
# {'a': 1, 'b': [1, 2]}

print(merge_dicts())
# {}
