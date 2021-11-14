# 切片同golang playes[start:end] 不包含end
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:3])
print(players[:3])
print(players[3:])
# 倒序打印 -3代表倒数第三个元素
print(players[-3:])


# 遍历切片
for player in players[:3]:
    print(player)
    
# 赋值列表sports = players[:] 如果是sports = players 相当于赋值给sports变量
# 则对sports的修改也会对players生效 而复制之后不会
sports = players[:]

message = "The first three iterms in the list are."
print(message.split(" ")[:3])
print(message.split(" ")[2:5])
print(message.split(" ")[-3:])