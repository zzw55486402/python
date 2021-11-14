# 类的定义形式 class Class_name():  类名首字母大写
class Dog():
    # 初始化函数 定义形式就是这样 不管是初始化函数还是方法都需要传入self 因为
    # 调用该函数必须有self self是自动传递的 我们不需要显示的传入
    def __init__(self, name, age):
        # 初始化属性name和age
        self.name = name
        self.age = age
    
    # 定义类中的方法
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")

# 根据类来创建实例 传入的参数是初始化函数中定义的参数 不需要传入self
dog = Dog("qaq", 2)
# 访问属性
print(dog.name)
print(dog.age)
# 调用方法
dog.sit()
dog.roll_over()

# 可以创建多个实例
dog1 = Dog("jerry", 2)
dog2 = Dog(age = 3, name = "tom")
dog1.sit()
dog2.roll_over()




class Car():
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        # 给属性指定默认值
        self.odometer_reading = 0

    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model
        return long_name.title() 

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    # 通过方法来修改属性值
    def update_odometer_reading(self, mileage):
        self.odometer_reading = mileage

    # 定义一个递增函数
    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 通过方法修改属性的值
my_new_car.update_odometer_reading(34)
my_new_car.read_odometer()

my_new_car.increment_odometer(42424)
my_new_car.read_odometer()