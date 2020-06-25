#import os                  # baris 1 & 2 sama saja artinya
from os import system # as windows maka: nanti jadi windows('cls')

def print_menu():
	print("Phonebook \n")
	print("[1] Phonelist")
	print("[2] Add Contact")
	print("[3] Delete Contact")
	print("[4] Searching Area")
	print("[5] Exit")

contactDict = {}
menu_option = 0

crash = False

while not crash :
	#os.system ('cls')
	system('cls') #'clear' untuk linux/ macos
	print_menu()
	menu_option = int(input("Option : "))

	if menu_option == 5:
		crash = True

	elif menu_option == 1:
		system('cls')
		print("Phonelist : \n")

		if len(contactDict) > 0:
			for contact in contactDict:
				print(f"Name : {contact}\t Phone number : {contactDict[contact]}")#\t Address : {contactDict[contact]["address"]}\t Relationship : {contactDict[contact]["re1"]}")
		input("Press [ENTER] to go back to the main menu")
	elif menu_option ==2:
		system('cls')
		print("Add Contact : \n")
		nama = input("Name \t:") #key
		nomor = input("Phone number \t: ") #val
		address = input("Address \t: ") #val
		re1 = input("Relationship \t: ") #val

		info = {} # ada dictionary dalam dictionary
		info["nomor"] = nomor
		info["address"]= address
		info["re1"] = re1

		contactDict["nama"] = info

		del info

		print("Contact has been saved !!")
		input("Click [ENTER] to go back to the main manu")
