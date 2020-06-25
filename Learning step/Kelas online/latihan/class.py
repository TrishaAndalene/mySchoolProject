"""
storing = list, dictionary, dan variabel

action = function def

"""
class food:

	def __init__(self, name, asal):
		self.name = name
		self.asal = asal

	def get_info(self):

		info = f"{self.name} is from {self.asal}."

		return info


food1 = food('Pasta', 'Italia')
food2 = food('Pempek', 'Palembang')

print(food1.get_info())
print(food2.get_info())

