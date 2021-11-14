# sort() 永久排序函数
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
# 反向
cars.sort(reverse= True)
print(cars)


# 临时排序函数sorted() 临时进行排序 不会影响原始数组
print(sorted(cars))
print(cars)
print(sorted(cars, reverse = False))

# 翻转列表 reverse() 永久的翻转list
cars.reverse
print(cars)

# 确定列表长度 len()
print(len(cars))