angka = 1
batas = 2
pengingat = 0

while angka <= batas:
	if angka % 2 != 0 and angka % 5 != 0:
		pengingat += 1
		print(angka)
	angka += 1

print("Jumlah bilangan bukan kelipatan 2 & 5 : ",(pengingat))