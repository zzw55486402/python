import json
# json.dump 将数据序列化并存储到文件中
file_path = "number.json"
numbers = [2, 3, 5, 7, 9, 11, 13]
with open(file_path, 'w') as file:
    # json.dump(数据, 文件标识符)
    json.dump(numbers, file)