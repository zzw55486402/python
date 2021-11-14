motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# 修改元素
motorcycles[0] = "ducati"
print(motorcycles)

# 添加元素到末尾append
motorcycles.append("honda")
print(motorcycles)

# 在任何位置插入元素 insert(index, value)
motorcycles.insert(0, "qianjiang")
print(motorcycles)

# 从列表中删除元素 del 删除指定位置的元素index pop 删除最后一个元素 元素会从list中消失
del motorcycles[0]
print(motorcycles)
# pop出来的元素可以赋值给m 将最后一个元素删除
m = motorcycles.pop()
print(motorcycles)
print(m)
print(motorcycles)
motorcycles.pop()
print(motorcycles)

# pop指定位置的元素pop(index) 该位置的元素会消失
m = motorcycles.pop(0)
print(m)
print(motorcycles)

# 根据值来删除元素 remove(value)
motorcycles.remove("yamaha")
print(motorcycles)