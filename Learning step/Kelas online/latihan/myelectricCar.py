from object2 import ElectricCar as EC


#using alias
my_tesla =EC('Tesla', 'XXX', 2020)
my_tesla.battery.describe_battery()

"""
my_tesla =ElectricCar('Tesla', 'XXX', 2020)
mr_bean_car = Car('British Leyland', 'Mini 100 Mark 4', 1977 )


my_tesla.battery.describe_battery()
print(mr_bean_car.get_descriptive_name())
"""