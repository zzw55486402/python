# 用""来定义字符串 'ada lovelace'
name = "'ada lovelace'"
# 用''来定义字符串 "ada lovelace"
name = '"ada lovelace"'
print(name)

# 字符串函数 title() upper() lower
# title() 首字母大写
name = "ada lovelace"
print(name.title())
# upper() 大写
print(name.upper())
# lower() 小写
print(name.lower())


# 拼接字符串 + 
first = "first_name"
last = "last_name"
name = first + " " + last
print(name)
message = first + " " + name.title() + " " + last
print(message)

# /t tab空格 /n换行 
print("\tpython")
print("python\ngo\njava\c++")

# 删除左右空格 lstrip() rstrip() strip()
message = " python  "
print(message.lstrip())
print(message.rstrip())
print(message.strip())