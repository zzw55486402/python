# 字典dict 相当于golang的map key-value 
# python的字典的value的值可以不同 相当于interface{}
alien = {"color":"green", "points":5}
print(alien["color"])
print(alien["points"])

# 添加一个键值对
alien["x_position"] = 0
alien["y_position"] = 25
print(alien)

# 创建空字典 然后添加一个键值对
alien = {}
alien["color"] = "red"
alien["position"] = 23
print(alien)

# 修改字典中的值
alien["color"] = "green"
print(alien)

# 删除键值对
del alien["color"]
print(alien)


# 遍历字典 通过alien.items()
alien["color"] = "green"
for k, v in alien.items():
    print(k, v)

# 遍历字典中的所有的键
for k in alien.keys():
    print(k)
    
# 遍历字典中的所有的值
for v in alien.values():
    print(v)
    
# 字典列表
alien_0 = {"color":"red", "position":0}
alien_1 = {"color":"green", "position":1}
alien_2 = {"color":"yellow", "position":2}
aliens = [alien_0, alien_1, alien_2]
print(aliens)
for alien in aliens:
    print(alien)
    

# 在字典中保存列表
pizza = {"crust":"thick", "toppings":["mushrooms", "extra cheese"]}
print(pizza["toppings"])
print(type(pizza["toppings"]))


# 在字典中保存字典

users = {
    "tom":{"height":180, "weight":80},
    "jerry":{"height":190, "weight":70},
}
print(users)

for k, v in users.items():
    print(k, v)




