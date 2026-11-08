nums = [3, 1, 4, 1, 5]
copy = nums[:]
print(nums == copy, nums is copy)  # True, False
nums[0] = 10

print(nums[0], copy[0])  # 10, 3
print(nums == copy, nums is copy)  # False, False
print(len(nums))  # 5

i = 0
count = 0
while i < len(nums):  # 10, 1, 4, 1, 5
    if nums[i] > 3:
        count += 1
    i += 1
    print(count, i)
print(count)  # 3
