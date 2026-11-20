def add_item(item, items: list = []):
    items.append(item)
    return items


print(add_item(1))  # [1]
print(add_item(2))  # [1,2] --> 意外！列表被共享了


# def counter():
#     count = 0

#     def increment():
#         count += 1

#     increment()  # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value


# counter()
