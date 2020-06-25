
jumlah = 0
banyak = 0
data = input("Masukkan nilainya :  ")


while data != "q" :
	data = float(data)
	banyak += 1
	jumlah += data
	data = input("Masukkan nilainya :  ")

#print(f"Jumlahnya {jumlah}")
#print(f"Banyaknya {banyak}")
print(f"Rata-rata = {jumlah/banyak}")
