from json import dump, load
from os import system
from time import sleep
from getpass import getpass

itemname = {}

itemprice = {}


def loadstat():
	global itemname, itemprice

	print("Loading data ...")
	sleep(3)
	with open ('user.json') as f:
		itemname = load(f)

	with open('contact.json') as f:
		itemprice = load(f)

	return True

def savedata():
	global itemname, itemprice

	with open('user.json', 'w') as f:
		dump(itemname, f)

	with open('contact.json', 'w') as f:
		dump(itemprice, f)


def loginpass():
	system('cls')
	print("Login")
	counter = 1
	nama = input("Name : ")
	sandi = getpass("Password : ")
	print("Checking name and password ...")
	datacheck = False
	passlogin = False
	if nama in itemname:
		datacheck = True
		passlogin = (itemname[nama] == sandi)
	while (not datacheck) or (not passlogin):
		counter += 1
		if counter > 3:
			return False
		print("Combination of name and password is wrong")
		nama = input("Name : ")
		sandi = getpass("Password : ")
		if nama in itemname:
			datacheck = True
			passlogin = (itemname[nama] == sandi)
	else:
		return True
		while False:
			nama = input("Name : ")
			sandi = getpass("Password : ")
			print("Checking name and password ...")
		

def menu():
	system('cls')
	print("Welcome to Item Reminder ! :)")
	input("[ENTER] to start")

def menu1():
	system('cls')
	print("Item Reminder System Apps")
	print("Choose wisely one of the choices beneath :")
	print("[1] Itemlist")
	print("[2] Add an item to itemlist")
	print("[3] Remove an item")
	print("[4] Search an item")
	print("[Q] Quit ")

def itemlist():
	system('cls')
	if len(itemprice) > 0:
		print("Itemlist :")
		for info in itemprice:
			print (f'Name \t: {info}\t Price \t: {itemprice[info]}')
	else:
		print("There is no item available now :(")	

	input("[ENTER] to continue")





def add():
	system('cls')
	print("Please input the item and its price")
	name = input("Name : \t")
	price = input("Price : ")

	itemprice[name] = price
	savedata()
	print("Saving ...")
	print("Do not turn of your computer/PC during this process")
	sleep(2)
	print("Data saved..")
	input("[ENTER] to go back ")


def rem():
	system('cls')
	print("Please input the item you want to remove")

	name = input("Name \t: ")

	if name in itemprice:
		del itemprice[name]
		savedata()
		print("Deleting item ...")
		print("Do not turn off your PC/computer during this process")
		sleep(1.5)
		print("Item has been deleted")

	else:
		print(f'{name} doesnot exists in itemlist')
	input("[ENTER] to go back")
	

def search():
	system('cls')
	print("Searching area ")

	name = input("The item you want to search: ")

	if name in itemprice:
		print(f'Item \t: {name}\t Price \t: {itemprice[name]}')
	else:
		print(f'{name} doesnot exist in itemlist')

	input("[ENTER] to go back")
	