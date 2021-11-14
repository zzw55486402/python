class Car():
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_Descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer!")
    def increment(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car need a gas tank!")

# 将电车中的属性单独抽取到一个类中 可以将该类的实例作为电车的一个属性
class Battery():
    def __init__(self, battery_size = 70) -> None:
        self.battery_size = battery_size
    def describe_battery(self):
        print("This ca has a " + str(self.battery_size) + "-KWh battery.")
# 继承 ()括号内填入对应的继承的类
# 并且自己的__init__函数还需要通过super().__init__ 来初始化父类
# 继承父类所有的属性和方法 初始化的时候需要初始化父类 并且需要传入父类的变量
# 创建子类时 父类必须包含在当前文件中 并且位于子类的前面
# 通过super()将父类进行初始化 这是继承中的一部分
class ElectricCar(Car):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        # 定义子类自己的属性
        self.battery_size = 70
        # 将其他类的实例作为该类的属性
        self.battery = Battery()
    # 子类可以拥有自己的方法
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
    # 重写父类的方法 只需要与父类的方法名相同即可
    def fill_gas_tank(self, battery):
        print("This car doesn not need a gas tank!" + "but need" + battery)




my_tesla = ElectricCar("tesla", "model_s", 2016)
print(my_tesla.get_Descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank("nanfu")

