#program Lingkaran
data = []


def luas_lingkaran(r):
	result = 3.14*r*r
	return result

def luas_segitiga(a,t):
	result = (a*t)/2
	return result

def ambil_data(namafile):
	listData = []
	"""
	with open(namafile) as f:
		lines = f.readlines()
	for line in lines:
		number = int(line.rstrip())
		listData.append(number)
	"""
	with open(namafile) as f:
		for line in f:
			listData.append(int(line.rstrip()))

	return listData


	#print(listData)

	

data = ambil_data("data.txt")
print(luas_segitiga(data[0], data[1]))
#print("Jarijari = ", jariJari)
#print("Luasnya = ", luas_lingkaran(jariJari))