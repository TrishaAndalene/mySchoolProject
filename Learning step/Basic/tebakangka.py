angkaTersimpan = 23
angkaDitebak = int(input("Masukkan Angkanya :"))

while angkaDitebak != angkaTersimpan :
	if angkaDitebak > angkaTersimpan :
		print("Terlalu besar")
	elif angkaDitebak < angkaTersimpan :
		print("Terlalu kecil")
	angkaDitebak = int(input("Masukkan Angkanya :"))
if angkaDitebak == angkaTersimpan :
	print("Selamat,Anda benar !")