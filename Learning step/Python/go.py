#number = 50
#number = int(input(""))
#number = #dari file data2.txt



def _luas_persegi(sisi):
	luas = sisi**2
	return luas

def _luas_persegipanjang(p,l):
	luas = p*l
	return luas 
def _ambil_data(path):
	with open(path) as f:
		number = int(f.read())
	return number
def _ambil_banyak_data(path):
	with open(path) as f:
		numbers = f.readlines()
	data = []
	for number in numbers:
		temp = number.rstrip()
		data.append(int(temp))
	del number, temp, numbers
	return data

rusukPersegi = _ambil_data("data4.txt")
datapersegipanjang = _ambil_banyak_data("data3.txt")

print(_luas_persegi(rusukPersegi))
print(_luas_persegipanjang(datapersegipanjang[0],datapersegipanjang[1]))