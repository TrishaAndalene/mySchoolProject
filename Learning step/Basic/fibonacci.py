a = int(input("Masukkan nilai a : "))
b = int(input("Masukkan nilai b : "))
print("a = ",a)
print("b = ",b)

while b <= 100 :
	print(a + b)
	a = a + b
	print(a + b)
	b += a