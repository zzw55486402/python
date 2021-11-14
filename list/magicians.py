# for循环打印list
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

print("\n")

for magician in magicians:
    print(magician.title() + ", is a great trick!")
    print(magician.title() + ", is a bigger cheater!\n")

print("\n")


# 数值list
# range(start, end) 产生start-end-1之间的数字
for num in range(1, 5):
    print(num)

# list(range(start, end)) 直接形成一个列表
numbers = list(range(1,5)) 
print(numbers)

# range 指定step步长 range(start, end, step)
steps = list(range(2, 11, 2))
print(steps)

# range() **
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)

# min() max() 打印list最小值和最大值 sum() 求和
digits = [1,2,3,4,5]
print(min(digits))
print(max(digits))
print(sum(digits))


# 列表解析 两部分 操作+数据(过滤条件) 操作：value ** 2 数据value 通过for循环来形成
squares = [value ** 2 for value in range(1, 11)]
print(squares)

for num in range(1, 21):
    print(num)
    
nums = [value for value in range(1, 1000001)]
# for num in nums:
#     print(num)
print(min(nums))
print(max(nums))
print(sum(nums))

odds = [value for value in range(1, 20, 2)]
for odd in odds:
    print(odd)
print("\n")
nums = [value for value in range(3, 31) if value % 3 == 0 ]
for num in nums:
    print(num)
print("\n")
nums = [num ** 3 for num in range(1, 11)]
for num in nums:
    print(num)
print("\n")