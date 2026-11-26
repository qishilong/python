# 请实现一个单链表类 `LinkedList`，支持以下操作：

# **需要实现的方法：**

# | 方法                     | 说明                                                         |
# | ------------------------ | ------------------------------------------------------------ |
# | `__init__(data=None)`    | 初始化空链表；`data` 可以是列表、元组或集合，其中的值会被初始化为链表的节点 |
# | `traverse(callback)`     | 遍历链表，对每个节点值调用 `callback(index, value)`          |
# | `__str__()`              | 返回链表的字符串表示，如 `"1 -> 2 -> 3"`                     |
# | `to_list()`              | 将链表转换为 Python 列表并返回                               |
# | `append(value)`          | 在链表尾部添加一个新节点                                     |
# | `prepend(value)`         | 在链表头部添加一个新节点                                     |
# | `insert(index, value)`   | 在指定索引位置插入新节点，索引从 0 开始                      |
# | `delete_by_value(value)` | 删除第一个值等于 `value` 的节点，返回是否删除成功            |
# | `delete_by_index(index)` | 删除指定索引位置的节点，返回被删除的值，索引越界时返回 `None` |
# | `find(value)`            | 查找值等于 `value` 的节点，返回其索引，不存在返回 -1         |
# | `get(index)`             | 获取指定索引位置的值，索引越界时返回 `None`                  |
# | `get_length()`           | 返回链表长度                                                 |
# | `is_empty()`             | 判断链表是否为空                                             |


# **示例用法：**

# ```python
# ll = LinkedList([1, 2, 3])
# print(ll)  # 输出: 1 -> 2 -> 3
# ll.append(4)
# print(ll)  # 输出: 1 -> 2 -> 3 -> 4
# ll.prepend(0)
# print(ll)  # 输出: 0 -> 1 -> 2 -> 3 -> 4
# ll.insert(2, 99)
# print(ll)  # 输出: 0 -> 1 -> 99 -> 2 -> 3 -> 4
# ll.traverse(lambda index, value: print(f"Index {index}: {value}"))
# print(ll.to_list())  # 输出: [0, 1, 99, 2, 3, 4]
# print(ll.find(99))  # 输出: 2
# print(ll.get(3))  # 输出: 2
# print(ll.delete_by_value(3))


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:
    """单链表"""

    def __init__(self, data=None):
        if data is None:
            return

        self.head: Node | None = None
        self._length = 0

        for value in data:
            self.append(value)

    def traverse(self, callback):
        current = self.head
        index = 0
        while current is not None:
            callback(index, current.value)
            current = current.next
            index += 1

    def __str__(self):
        node_list = self.to_list()

        str = f"{node_list[0]}"

        for value in node_list[1:]:
            str += f" -> {value}"

        return str

    def to_list(self):
        if self.head is None:
            return []

        current = self.head
        node_list = [current.value]

        while current.next is not None:
            current = current.next
            node_list.append(current.value)

        return node_list

    def append(self, value):
        new_node = Node(value, None)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node

        self._length += 1

    def prepend(self, value):
        new_node = Node(value, None)
        new_node.next = self.head
        self.head = new_node

        self._length += 1

    def insert(self, index, value):
        if index < 0 or index > self._length:
            return

        new_node: Node = Node(value, None)
        current = self.head

        if index == 0:
            self.prepend(value)
            return

        if current is None:
            self.head = new_node
        else:
            while index > 1:
                current = current.next
                index -= 1

        new_node.next = current.next
        current.next = new_node

        self._length += 1

    def delete_by_value(self, value):
        if self.head is None:
            return False

        current = self.head

        if self.head.value == value:
            current = current.next
            self.head = current
            self._length -= 1
            return True
        else:
            if current.next is None:
                return False

            while current.next.value != value:
                current = current.next

            if current is None:
                return False

            current.next = current.next.next
            self._length -= 1
            return True

    def delete_by_index(self, index):
        if index < 0 or index > self._length or self.head is None:
            return

        delete_value = None

        if index == 0:
            delete_value = self.head.value
            self.head = self.head.next
            self._length -= 1
            return delete_value

        current = self.head

        i = 0
        while i < index - 1:
            current = current.next
            i += 1

        delete_value = current.next.value
        current.next = current.next.next
        self._length -= 1
        return delete_value

    def find(self, value):
        if self.head is None:
            return -1

        current = self.head

        result = -1
        index = 0
        while current is not None:
            if current.value == value:
                result = index
                break

            current = current.next
            index += 1

        return result

    def get(self, index):
        if index < 0 or index > self._length or self.head is None:
            return

        if index == 0:
            return self.head.value

        current = self.head

        while index > 0:
            current = current.next
            index -= 1

        return current.value

    def get_length(self):
        return self._length

    def is_empty(self):
        return self._length == 0


ll = LinkedList([1, 2, 3])
print(ll)  # 输出: 1 -> 2 -> 3
print(ll._length)
ll.append(4)
print(ll)  # 输出: 1 -> 2 -> 3 -> 4
print(ll._length)
ll.prepend(0)
print(ll)  # 输出: 0 -> 1 -> 2 -> 3 -> 4
print(ll._length)
ll.insert(2, 99)
print(ll)  # 输出: 0 -> 1 -> 99 -> 2 -> 3 -> 4
print(ll._length)
ll.traverse(lambda index, value: print(f"Index {index}: {value}"))
print(ll.to_list())  # 输出: [0, 1, 99, 2, 3, 4]
print(ll.find(99))  # 输出: 2
print(ll.get(3))  # 输出: 2
print(ll.delete_by_value(3))
print(ll, ll._length)
