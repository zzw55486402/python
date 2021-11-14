# 在此模块中导入pizza as 指定别名
import pizza as p

# 导入特定的函数
from pizza import make_pizza

# 指定别名
from pizza import make_pizza as mp

# 导入所有的函数 import *
from pizza import *

p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

make_pizza(14, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

mp(15, "pepperoni")
mp(12, "mushrooms", "green peppers", "extra cheese")