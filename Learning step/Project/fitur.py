import os
import time

data = []

def _main_menu():
	os.system("cls")
	print("Notes Writer \n")
	print("[1] Write notes")
	print("[2] Checking notes")
	print("[3] Delete notes")
	print("[4] Exit")

def _buat_catatan():
	os.system("cls")
	print("Buat Catatan disini : \n")
	catatan = input()
	data.append(catatan)
	print("Catatan Tersimpan")
	time.sleep(1.5)

def _lihat_catatan():
	os.system("cls")
	if len(data) > 0:
		print("Daftar catatan yang sudah dibuat :")
		for catatan in data:
			print(catatan)
		input("Tekan [enter] untuk kembali ke menu utama")
	else:
		print("Catatan belum ada")
		input("Tekan [enter] untuk kembali ke menu utama")