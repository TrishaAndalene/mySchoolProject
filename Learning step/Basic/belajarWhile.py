UsernameTersimpan = "Unknown"
PasswordTersimpan = "281006"
UsernameYangDimasukkan = input("Masukkan Username Anda : ")
PasswordYangDimasukkan = input("Masukkan Password Anda : ")
Counter = 1

while PasswordYangDimasukkan != PasswordTersimpan or UsernameYangDimasukkan != UsernameTersimpan :
	print("Username atau Password salah")
	Counter += 1
	if Counter == 5 :
		print("Cobalah beberapa saat lagi..")
		break
	UsernameYangDimasukkan = input("Masukkan Username Anda : ")
	PasswordYangDimasukkan = input("Masukkan Password Anda : ")

if PasswordYangDimasukkan == PasswordTersimpan and UsernameYangDimasukkan == UsernameTersimpan :
	print("Welcome back ...")