# 写入文件 open(文件路径, 模式)
# 模式包括 读取r 写入w 附加模式（不覆盖写入）a 或者读写模式r+
# 忽略则是只读
# 这样的写入是覆盖写入
filename = "programming.txt"
with open(filename, 'w') as file:
    file.write("this is a doc")

# 非覆盖写入
filename = "text.txt"
with open(filename, "a") as file:
    file.write("gogogo\n")
    file.write("Let is go G2\n")