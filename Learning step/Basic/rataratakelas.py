

def _ambil_banyak_data(path):
	with open(path) as f:
		numbers = f.readlines()
	data = []
	for number in numbers:
		temp = number.rstrip()
		data.append(int(temp))
	return data
"""
	for number in data:
		x = 0
		x += number
		y = 0
		y += len(data)
		z = x/y
	del number ,numbers ,temp ,data ,x ,y
	return z
"""
def _rata(path):
	jumlah = 0
	with open(path) as f:
		numbers = f.readlines()
		datas = []
		for number in numbers:
			datas.append(int(number.rstrip()))
		for data in datas:
			jumlah += data
		mean = jumlah/len(numbers)
	return mean

data7 = _ambil_banyak_data("datakelas7.txt")
mean7 = _rata("datakelas7.txt")
print("Rata-rata kelas 7 : ", mean7)
data8 = _ambil_banyak_data("datakelas8.txt")
mean8 = _rata("datakelas8.txt")
print("Rata-rata kelas 8 : ", mean8)
data9 = _ambil_banyak_data("datakelas9.txt")
mean9 = _rata("datakelas9.txt")
print("Rata-rata kelas 9 : ", mean9)