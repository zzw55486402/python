import json

# 通过json.load() 将json文件读取到内存中
filename = "number.json"
with open(filename) as file:
    numbers = json.load(file)
print(numbers)