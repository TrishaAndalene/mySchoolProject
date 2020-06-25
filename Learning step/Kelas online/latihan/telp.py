

class Battery:

	def __init__(self, battery_size = 125):
		self.battery_size = battery_size

	def desc_battery(self):
		print(f"This phone's battery size is {self.battery_size}")


class Phone:

	def __init__(self, brand, color):

		self.brand = brand
		self.color = color
		self.battery = Battery()

	def desc_info_name(self):
		info = f"{self.brand} - {self.color}"
		return info





