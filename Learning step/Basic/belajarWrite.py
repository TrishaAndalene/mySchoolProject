#angka1, angka2, angka3 = input().split()

"""
with open("data.txt", "w") as f:
	f.write(str(angka)) #str = membuat int jadi string
"""

daftarNilai = []

for i in range(6):
	data = input()
	daftarNilai.append(data)

with open("data.txt", "a") as f:
	for nilai in daftarNilai:
		f.write(str(nilai+"\n"))
