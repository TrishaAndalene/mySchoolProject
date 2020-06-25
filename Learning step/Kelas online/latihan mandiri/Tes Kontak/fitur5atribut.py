from os import system
from json import load, dump
from getpass import getpass
from time import sleep

user = {}

item = {}


def loadstat():
	global user, item

	with open ('nama5atributdepan.json') as f:
		user = load(f)

	with open ('password.json') as f:
		item = load(f)


	return True

def save():
	global user, item

	with open ('nama5atributdepan.json', 'w') as f:
		dump(user, f)

	with open ('password.json', 'w') as f:
		dump(item, f)

def loginpas():
	system('cls')
	print("Contact Application")
	input("Press [enter] to login")
	system('cls')
	print("Login :")
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
		