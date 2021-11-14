cars = ["audi", "bmw", "subaru", "toyota"]
# if-else 结构
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# and => && 
# or => ||

# 特定值是否在list中 if "bmw" in cars:
# 特定值是否不在list中 if "honda" not in cars:

# bool表达式
flag = True
flag = False
if 1 <= 2 :
    print("yes")
    
# if-elif-else结构
age = 13
if age < 4:
    print("kid")
elif age < 8:
    print("big kid")
else:
    print("people")
    
# if-elif-elif-elif-else  else 可以省略

# 判断列表是否为空
if cars:
    print(cars)
else:
    print("empty")