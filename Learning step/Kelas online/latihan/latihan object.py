class Student:

	def __init__(self, name, nickname, grade, age, study):
		self.name = name
		self.nickname = nickname
		self.grade = grade
		self.age = age
		self.study = study

student1 = Student('Jesse Ario', 'Jesse', 8, 14, 'IPS')

print(f"Halo ini teman saya namanya {student1.name}")
print(f"Kamu dapat memanggilnya {student1.nickname}")
print(f"Umurnya {student1.age} tahun dan dia menduduki kelas {student1.grade}")
print(f"Pelajaran kesukaannya adalah {student1.study}")
