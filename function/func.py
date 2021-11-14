# function 定义函数
def greet_user():
    print("user is health")
greet_user()

# 函数增加参数
def greet_user_name(username):
    print(username + " user is health")
greet_user_name("zzw")


# 传递实参 位置实参和关键字实参

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("I have a pet, it is name is " + pet_name + ".")
# 位置实参 传入的参数对应函数对应的顺序
describe_pet("dog", "lily")
describe_pet("cat", "juice")

# 关键字实参 通过指定对应的参数传入对应的值
describe_pet(pet_name = "tom", animal_type = "cat")
describe_pet(animal_type = "dog", pet_name = "xuan")

# 参数默认值必须放在参数的最后面 调用函数的时候可以不传入该值 则使用默认值 也可以传入 则使用传入的值
def describe_pets(pet_name, animal_type = "dog"):
    print("\nI have a " + animal_type + ".")
    print("I have a pet, it is name is " + pet_name + ".")

describe_pets("tom")
describe_pets("jerry", animal_type = "cat")

# 函数的调用可以使用默认值+位置参数+关键字参数混用的形式



# 返回对应的值 return 不需要显示的指定参数
def get_formatted_name(first_name, last_name):
    full_name = first_name + "_" + last_name
    return full_name.title()
full_name = get_formatted_name("z", "zw")
print(full_name)


# 返回字典
def build_person(first_name, last_name):
    full_name = {"first_name": first_name, "last_name":last_name}
    return full_name
full_name = build_person("zzw", "qaq")
print(full_name)


# 传递列表
def greet_users(names):
    for name in names:
        msg = "Hello, " + name + " I love you!"
        print(msg)
names = ["lily", "tom", "tony"]
greet_users(names)

# 在函数中修改list 因为python传入的列表是可以进行修改的，是对原列表有效的 同golang
def change_name(names):
    names[0] = 'qwq'
    names[1] = 'qaq'
change_name(names)
print(names)

# 如果不想列表被修改，那么就传入列表的copy
def change_name_copy(names):
    names[0] = "qvq"
    names[1] = "zzw"
    print(names)
change_name_copy(names[:])
print(names)

# 或者 在函数内部进行copy 这样也不会对原列表产生影响
def change_name_copy2(names):
    users = names[:]
    users[0] = "qxq"
    users[1] = "zxw"
    print(users)
change_name_copy2(names)
print(names)


# 可变参数 *参数名 将参数封装在一个元祖中 可变参数必须放在最后，且必须只能有一个
def make_pizza(size, *toppings):
    print(toppings)

make_pizza(12, "personal")
make_pizza(13, "personal", "people", "zzw")

def make_pizza_two(*toppings):
    for topping in toppings:
        print("-" + topping)
make_pizza_two("personal")
make_pizza_two("personal", "people", "zzw")


# 传入关键字实参 **user_info
def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile
profile = build_profile("zzw", "qaq", height = 17, weight = 20)
print(profile)