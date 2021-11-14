# 从其他文件中引入类Car使用
from car import Car
from car import ElectricCar
# 导入整个car
import car
# 导入所有类
from car import *
from car import Car, ElectricCar, Battery
my_new_car = Car("tesla", "a4", 2018)
print(my_new_car.get_descriptiven_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

electric_car = ElectricCar("tesla", "model_s", 2021)
print(electric_car.get_descriptiven_name())
electric_car.describe_battery()
electric_car.get_range()