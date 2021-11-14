# 异常
# print(5 / 0)

# 异常处理：try-except-else代码块
# else 可选
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can not divide by zero!")

# 文件不存在异常 FileNotFoundError