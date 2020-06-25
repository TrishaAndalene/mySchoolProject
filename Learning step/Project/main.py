import fitur

usernametersimpan = "unknown"
passwordtersimpan = "123456"
usernameyangdimasukkan = input("Masukkan username :")
passwordyangdimasukkan = input("Masukkan password :")

while passwordyangdimasukkan != passwordtersimpan or usernameyangdimasukkan != usernametersimpan :
	print("The username or the password isn't true")

	usernameyangdimasukkan = input("Masukkan username :")
	passwordyangdimasukkan = input("Masukkan password :")

print("Welcome back user")

def _main_menu():
	print("Notes Writer \n")
	print("[1] Make notes")
	print("[2] Look notes")
	print("[3] Delete notes")
	print("[4] Exit")

userInput = "0"
while userInput != "4":
	fitur._main_menu()
	print("what can I help you? ")
	userInput = input("Pilihan Menu :")
	if userInput == "1":
		fitur._buat_catatan()
	if userInput == "2":
		fitur._lihat_catatan()

if userInput == "4":
	print("Thank you for trying our application! :)")





