call_count = 0


def process_data(data):
    result = sum(data)
    # 处理完成后递增计数器
    global call_count
    call_count += 1
    return result


print(process_data([1, 2, 3]))  # 6
print(process_data([4, 5, 6]))  # 15
print(f"总共调用了 {call_count} 次")  # 总共调用了 2 次
