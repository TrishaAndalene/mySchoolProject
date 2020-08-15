from json import dump, load
from os import system
from time import sleep
from getpass import getpass

user = {}

item = {}


def loadstat():
	global user, item

	print("Starting engine ...")
	sleep(3)
	with open ('user.json') as f:
		user = load(f)

	with open('contact.json') as f:
		item = load(f)

	return True

def savedata():
	global user, item

	with open('user.json', 'w') as f:
		dump(user, f)

	with open('contact.json', 'w') as f:
		dump(item, f)


def loginpass():
	system('cls')
	print("Login")
	counter = 1
	nama = input("Name : ")
	sandi = getpass("Password : ")
	print("Checking name and password ...")
	sleep(2)
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
		input("[Enter] to retry")
		system('cls')
		print("Login")
		nama = input("Name : ")
		sandi = getpass("Password : ")
		if nama in user:
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
	print("Item Reminder for Shopping System Apps")
	print("Choose wisely one of the choices beneath :")
	print("[1] Itemlist")
	print("[2] Add an item to itemlist")
	print("[3] Remove an item")
	print("[4] Search an item")
	print("[Q] Quit ")

def menu2():
	system('cls')
	print("Test Project System Apps :)")
	print("Apps collection :")
	print("[1] Item Reminder")
	print("[2] Temperature Converter")
	print("[Q] Quit Application")

def menu3():
	system('cls')
	print("Temperature Converter System Apps ")
	print("From what :")
	print("[1] Celcius")
	print("[2] Reamur")
	print("[3] Fahrenheit")
	print("[4] Kelvin")
	print("[Q] Quit")

def cel():
	system('cls')
	print("Temperature Converter System Apps ")
	print("To what : ")
	print("[1] Reamur")
	print("[2] Fahrenheit")
	print("[3] Kelvin")
	print("[4] Quit")


def rea():
	system('cls')
	print("Temperature Converter System Apps ")
	print("To what : ")
	print("[1] Celcius")
	print("[2] Fahrenheit")
	print("[3] Kelvin")
	print("[4] Quit")

def far():
	system('cls')
	print("Temperature Converter System Apps ")
	print("To what : ")
	print("[1] Celcius")
	print("[2] Reamur ")
	print("[3] Kelvin")
	print("[4] Quit")


def kel():
	system('cls')
	print("Temperature Converter System Apps ")
	print("To what : ")
	print("[1] Celcius")
	print("[2] Reamur ")
	print("[3] Fahrenheit")
	print("[4] Quit")



def cel1():
	system('cls')
	a = int(input("Please input the temperature : "))
	b = a*4/5
	print("Calculating ...")
	sleep(2)
	print(f"In Reamur, the temperature is {b}")
	input("[Enter] to continue")


def cel2():
	system('cls')
	a = int(input("Please input the temperature : "))
	b = (a*9/5) + 32
	print("Calculating ...")
	sleep(2)
	print(f"In Fahrenheit, the temperature is {b}")
	input("[Enter] to continue")


def cel3():
	system('cls')
	a = int(input("Please input the temperature : "))
	b = a + 273
	print("Calculating ...")
	sleep(2)
	print(f"In Kelvin, the temperature is {b}")
	input("[Enter] to continue")


def rea1():
	system('cls')
	a = int(input("Please input the temperature : "))
	b = a*5/4
	print("Calculating ...")
	sleep(2)
	print(f"In Celcius, the temperature is {b}")
	input("[Enter] to continue")

def rea2():
	system('cls')
	a = int(input("Please input the temperature : "))
	b = (a*9/4) + 32
	print("Calculating ...")
	sleep(2)
	print(f"In Fahrenheit, the temperature is {b}")
	input("[Enter] to continue")

def rea3():
	system('cls')
	a = int(input("Please input the temperature : "))
	b = (a*5/4) + 273
	print("Calculating ...")
	sleep(2)
	print(f"In Kelvin, the temperature is {b}")
	input("[Enter] to continue")

def far1():
	system('cls')
	a = int(input("Please input the temperature : "))
	b = (a - 32)*5/9
	print("Calculating ...")
	sleep(2)
	print(f"In Celcius, the temperature is {b}")
	input("[Enter] to continue")

def far2():
	system('cls')
	a = int(input("Please input the temperature : "))
	b = (a - 32)*4/9
	print("Calculating ...")
	sleep(2)
	print(f"In Reamur, the temperature is {b}")
	input("[Enter] to continue")

def far3():
	system('cls')
	a = int(input("Please input the temperature : "))
	b = ((a - 32)*5/9) + 273
	print("Calculating ...")
	sleep(2)
	print(f"In Kelvin, the temperature is {b}")
	input("[Enter] to continue")


def kel1():
	system('cls')
	a = int(input("Please input the temperature : "))
	b = a - 273
	print("Calculating ...")
	sleep(2)
	print(f"In Celcius, the temperature is {b}")
	input("[Enter] to continue")

def kel2():
	system('cls')
	a = int(input("Please input the temperature : "))
	b = (a - 273)*4/5
	print("Calculating ...")
	sleep(2)
	print(f"In Reamur, the temperature is {b}")
	input("[Enter] to continue")

def kel3():
	system('cls')
	a = int(input("Please input the temperature : "))
	b = ((a - 32)*9/5) + 32
	print("Calculating ...")
	sleep(2)
	print(f"In Fahrenheit, the temperature is {b}")
	input("[Enter] to continue")


def itemlist():
	system('cls')
	if len(item) > 0:
		print("Itemlist :")
		for info in item:
			print (f'Name \t: {info}\t Total \t: {item[info]}')
	else:
		print("There is no item available now :(")	

	input("[ENTER] to continue")





def add():
	system('cls')
	print("Please input the item and its price")
	name = input("Name : \t")
	price = input("Total : ")

	item[name] = price
	savedata()
	system('cls')
	print("Saving .")
	print("Do not turn off your PC/computer during this process")
	sleep(1)
	system('cls')
	print("Saving ..")
	print("Do not turn off your PC/computer during this process")
	sleep(1)
	system('cls')
	print("Saving ...")
	print("Do not turn off your computer/PC during this process")
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
		system('cls')
		print("Deleting item .")
		print("Do not turn off your PC/computer during this process")
		sleep(1)
		system('cls')
		print("Deleting Item ..")
		print("Do not turn off your PC/computer during this process")
		sleep(1)
		system('cls')
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
		print(f'Item \t: {name}\t Total \t: {item[name]}')
	else:
		print(f'{name} doesnot exist in itemlist')

	input("[ENTER] to go back")