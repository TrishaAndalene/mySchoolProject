#store data struktur data python -> variable, list, dict & object
#json -> javascript object notation
#object : berupa benda fisik / abstrak
#contoh :
'''
nama = "JONOJONI"
dataList = ['JONOJONI', 20]
#data berupa atribut

#behavior method -> function / fungsi(f(x))

class Dog :

	def __init__(self, name, age):
		self.name = name
		self.age = age #month

susi_dog = Dog('Wili', 2)

print(f"Halo ini adalah {susi_dog.name}")
print(f"Usianya {susi_dog.age} bulan ")

class pen:

	def __init__(self, merk, model, color):
		self.merk = merk
		self.model = model
		self.color = color

#create object
penNumber1 = pen("PILOT", "Hi-Tech", "Purple")

print(f"")