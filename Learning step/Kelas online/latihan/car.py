class Car:
	#ini object kelas car/mobil yang sederhana

	def __init__(self, brand, model, year):
		self.brand = brand
		self.model = model
		self.year = year 
		self.odometer_reading = 0 #konstanta

	def get_info(self):
		desc = f"{self.year} - {self.brand} - {self.model}"
		return desc

	def read_odometer(self):
		res = f"Odometer = {self.odometer_reading}"
		return res

	def update_odometer(self, km):
		if km >= self.odometer_reading:
			self.odometer_reading = km
		else:
			print("Odometer can't roll back")

	def increment_odometer(self, add):
		self.odometer_reading += add

#instance as atribut
class Battery:

	def __init__(self, battery_size = 75):
		self.battery_size = battery_size


class Color:

	def __init__(self, car_color = 'purple'):
		self.car_color = car_color






class MobilListrik(Car):

	def __init__(self, brand, model, year, charger_type):
		super().__init__(brand, model, year)
		self.charger_type = charger_type
		self.battery = Battery()
		self.color = Color()

	def get_info(self):
		desc = f"{self.year} - {self.brand} - {self.model} - {self.charger_type} - {self.color}"
		return desc

	#def get_info_battery(self):
		#print(f"This car has a {self.battery_size}-kWh battery")


#membuat instance (ciptaan)
"""
mobil_sir_anas = Car('Toyota', 'Kijang', 1999)

print(mobil_sir_anas.get_info()) 
mobil_sir_anas.increment_odometer(3)
mobil_sir_anas.increment_odometer(100)
mobil_sir_anas.update_odometer(0)
print(mobil_sir_anas.read_odometer())
"""

mobillistriksaya = MobilListrik('Tesla', 'Super Car', 2019, 'Singapore Lincense')
print(mobillistriksaya.get_info())

