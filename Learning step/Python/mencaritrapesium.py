

def _ambil_banyak_data(path):
	with open(path) as f:
		numbers = f.readlines()
	data = []
	for number in numbers:
		temp = number.rstrip()
		data.append(int(temp))
	del number, temp, numbers
	return data

def _luas_trapesium(a,b,t):
	res = ((a+b)*t)/2
	return res

dataTrap1 = _ambil_banyak_data("datatrapesium1.txt")
luasTrap1 = _luas_trapesium(dataTrap1[0],dataTrap1[1],dataTrap1[2])
print("Luas trapesium 1 = %i" % luasTrap1)
dataTrap2 = _ambil_banyak_data("datatrapesium2.txt")
luasTrap2 = _luas_trapesium(dataTrap2[0],dataTrap2[1],dataTrap2[2])
print("Luas trapesium 2 = %i" % luasTrap2)
dataTrap3 = _ambil_banyak_data("datatrapesium3.txt")
luasTrap3 = _luas_trapesium(dataTrap3[0],dataTrap3[1],dataTrap3[2])
print("Luas trapesium 3 = %i" % luasTrap3)