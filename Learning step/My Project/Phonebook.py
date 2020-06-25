import os


"""
with open("data2.txt") as f :
	for nama in Phone_list:
		f.write(str(nilai+"\n"))
"""
with open("data2.txt") as f :
			f.read(str{k,v})

def print_menu():
	os.system("cls")
	print("[1] See telephone number")
	print("[2] Add contact")
	print("[3] Delete contact")
	print("[4] Search contact")
	print("[5] Load telephone number")
	print("[6] Save contact")
	print("[7] Exit application")

def print_number(a):
	os.system("cls")
	print("Phone list : ")
	for k,v in Phone_list.items():
			print(f"Name : {k} , Telephone number : {v}")
		#with open("data2.txt") as f :
			#f.write(k+"\n")
			#f.write(str(v+"\n"))

	input("Press [enter] to go back to the menu ")

def add_number(nama,no,Phone_list):
	Phone_list[nama] = no
	print("Phone number saved :)")
	#with open("data2.txt") as f :
			#.read(str(nama))
			#f.read(str(no))
	input("Press [enter] to go back to the menu ")

def hapus_kontak(nm):
	if nm in Phone_list:
		del Phone_list[nm]
		print("Phone number has been deleted :)")
		input("Press [enter] to go back to the menu ")

def cari_kontak(nm):
	if nm in Phone_list:
		print("Complete identity : ")
		print("Name \t\t: ", nm)
		print("Phone number \t: ", Phone_list[nm])
	else:
		print("No contact related to the contact you search :(")
	input("Press [enter] to go back to the menu ")
Phone_list = {}
Choice_menu = 0
print_menu()

while Choice_menu != 7 :
	Choice_menu = int(input("Options : "))
	if Choice_menu == 1:
		os.system("cls")
		print_number(Phone_list)
		print_menu()
	elif Choice_menu == 2:
		os.system("cls")
		print("Add contact")
		nama = input("Insert name : ")
		no = input("Insert the telephone number : ")
		add_number(nama,no,Phone_list)
		print_menu()
	elif Choice_menu == 3:
		os.system("cls")
		print("Delete contact")
		nm = input("Insert the name of the number : ")
		hapus_kontak(nm)
		print_menu()
	elif Choice_menu == 4:
		os.system("cls")
		nama = input("Insert the name you search : ")
		cari_kontak(nama)
		print_menu()

	
if Choice_menu == 7:
		print("Thank you for trying ")


with open("data2.txt") as f :
		f.write(k+"\n")
		f.write(str(v+"\n"))
