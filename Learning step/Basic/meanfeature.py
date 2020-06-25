

def _ambil_banyak_data(path):
	with open(path) as f:
		numbers = f.readlines()
	data = []
	for number in numbers:
		temp = number.rstrip()
		data.append(int(temp))
	del number ,temp ,numbers
	return data

def _banyak_data(path):
	with open(path) as f:
		numbers = f.readlines()
	data1= []
	for number in numbers:
		temp1 = number.rstrip()
		data1.append(len(temp1))
	del number ,temp1 ,numbers
	return data1



datakelas7 = _ambil_banyak_data("datakelas7.txt")
for data in datakelas7:
	info71 = 0
	info71 += data
jumlah7 = _banyak_data("datakelas7.txt")
info7 = 0
info7 += len(jumlah7)
print(f"Rata-rata kelas 7 = ", {info71/info7})


