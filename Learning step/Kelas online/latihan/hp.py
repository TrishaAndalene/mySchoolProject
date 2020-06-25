
class Battery:

	def __init__(self, battery_size = 100):
		self.battery_size = battery_size

class charger:

	def __init__(self, charging_time = 30):
		self.charging_time = charging_time


class Hp:

	def __init__(self, brand, year):
		self.brand = brand
		self.year = year
		self.battery_size = Battery()
		self.charging_time = charger()

	def get_info(self):
		desc = f"{self.brand} - {self.year} -{self.battery_size} - {self.charging_time} "
		return desc


Hpsaya = Hp('Samsung', 2019)
print(f"{Hpsaya.get_info()}")



