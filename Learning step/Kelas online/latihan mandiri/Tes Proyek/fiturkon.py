from json import dump, load
from os import system
from time import sleep
from getpass import getpass

user = {}

item = {}


def loadstat():
	global user, item

	print("Loading data ...")
	sleep(3)
	with open ('user1.json') as f:
		user = load(f)

	with open('contact1.json') as f:
		item = load(f)

	return True

def savedata():
	global user, item

	with open('user1.json', 'w') as f:
		dump(user, f)

	with open('contact1.json', 'w') as f:
		dump(item, f)


def loginpass():
	system('cls')
	print("Login")
	counter = 1
	nama = input("Name : ")
	sandi = getpass("Password : ")
	print("Checking name and password ...")
	datacheck = False
	passlogin = False
	if nama in user:
		datacheck = True
		passlogin = (user[nama] == sandi)
	while (not datacheck) or (not passlogin):
		counter += 1
		if counter > 3:
			return False
		print("Combination of name and password is wrong")
		nama = input("Name : ")
		sandi = getpass("Password : ")
		if nama in itemname:
			datacheck = True
			passlogin = (user[nama] == sandi)
	else:
		return True
		while False:
			nama = input("Name : ")
			sandi = getpass("Password : ")
			print("Checking name and password ...")
		

def menu():
	system('cls')
	print("Welcome to my Test Project ! :)")
	input("[ENTER] to start")

def menu1():
	system('cls')
	print("Personal information Apps")
	print("Choose wisely one of the choices beneath :")
	print("[1] Information list")
	print("[2] Add a name to information list")
	print("[3] Remove name")
	print("[4] Search name")
	print("[Q] Quit ")


def itemlist():
	system('cls')
	if len(item) > 0:
		print("Itemlist :")
		for info in item:
			print (f' Front name \t: {info}\t Back name \t: {info}  Phone number : {item[info]}   Email : {item[info]}   Id : ')
	else:
		print("There is no item available now :(")	

	input("[ENTER] to continue")





def add():
	system('cls')
	print("Please input the item and its price")
	front = input("Front : ")
	back = input("Back : ")
	price = input("Phone number : ")
	name = front + " " + back
	email = front + "." + back + "@igs.com"
	Idpass = "igs-" + price[0:4] 
	item[name,email,Idpass] = price
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

	if name in item:
		del item[name]
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

	if name in item:
		print(f'Item \t: {name}\t Price \t: {item[name]}')
	else:
		print(f'{name} doesnot exist in itemlist')

	input("[ENTER] to go back")