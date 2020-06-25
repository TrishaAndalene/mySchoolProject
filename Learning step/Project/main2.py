import fitur


userInput = "0"
while userInput != "4":
	fitur._main_menu()
	userInput = input("Pilihan Menu :  ")
	if userInput == "1":
		fitur._buat_catatan()
	if userInput == "2":
		fitur._lihat_catatan()

print("Aplikasi Catatan")

def _main_menu():
	print("[1] Buat Catatan")
	print("[2] Lihat Catatan")
	print("[3] Hapus Catatan")
	print("[4] Keluar dari aplikasi")

