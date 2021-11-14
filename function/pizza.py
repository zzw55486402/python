# 将函数存储在模块中进行导入
def make_pizza(size, *toppings):
    print("\nmakeing a " + str(size) + 
            "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
