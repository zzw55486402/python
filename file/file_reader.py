# 打开并读取文件 通过with open(文件路径) as 别名: 即可
# 通过with open 可以不用显示的关闭文件
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents)


# 路径：相对于该运行文件的路径
file_path = "text_files/filename.txt"
with open(file_path) as file:
    # 逐行读取文件
    for line in file:
        print(line)

# 将文件内容保存到lines列表中 通过readlines()来读取就可以
with open(file_path) as file:
    lines = file.readlines()
print(lines)
for line in lines:
    print(line)

