#Objek -> sebuah instance (hal yang nyata) ciptaan / creation
#- menyimpan data dengan memanfaatkan struktur data dasar dari python
#- mengolah dan membuat fungsi atau activity dengan function (def)
#- menggabungkan storing data dan activity / method dengan OBJECT
#- Module = OBJECT

#ex:
"""
Game > Alien VS Space Shuttle
Object > Ship(shuttle), Alien, Bullet, Meteor
OOP(Object Oriented programming)

"""

#ex(car.py):
"""
Mobil :
1. mobil biasa
2. mobil listrik


"""

class Car:

	def __init__(self, make, model, year):

		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f" {self.year} - {self.make} - {self.model}"
		return long_name

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} Km on it")

	def update_odometer(self, kms):
		if kms >= self.odometer_reading :
			self.odometer_reading = kms
		else:
			print("Cannot roll back odometer")


	def increment_odometer(self, kms):
		self.odometer_reading += kms

class Battery:
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh")




class ElectricCar(Car):

	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery(100)