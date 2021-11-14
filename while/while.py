
# while 循环
current = 1
while current <= 5:
    print(current)
    current += 1

# break退出
current = 1
while current <= 10:
    current += 1
    if current % 3 == 0:
        continue
    elif current % 2 == 0:
        print(current)

# while循环处理列表和字典
users = ["alice", "brain", "candace"]
# 弹出元素并打印
while users:
    user = users.pop()
    print(user)
print(users)

# 删除值对应的元素
users = ["alice", "brain", "candace"]
while "alice" in users:
    users.remove("alice")
print(users)

# 使用用户输入来填充字典
response = {}
flag = True
index = 0
while flag:
    name = input("Tell me your name: ")
    response["name_" + str(index)] = name
    age = input("Tell me your age: ")
    response["age_" + str(index)] = int(age)
    if name == "zzw":
        flag = False
    index += 1
print(response)