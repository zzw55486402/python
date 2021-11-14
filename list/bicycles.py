# list 列表就是数组也就是golang中的切片
bicycles = ['trek', 'cannondale', 'readline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

message = "My first bicycke was a " + bicycles[0].title() + "."
print(message)

names = ["zzw", "zzc", "zzl"]
message = " are you ok?"
print(names[0] + message)
print(names[1] + message)
print(names[2] + message)