from os import system
from json import dump, load
from time import sleep

user = {}

itemname = {}

price = {}

total = {}

fileitem = "user.json"
fileprice = "contact.json"
filetotal = "total.json"

def loadstat():
	print("Loading data ...")
	with open (fileitem) as f:
		itemname = load(f)
	with open(fileprice) as f:
		price = load(f)
	with open (filetotal) as f:
		total = load(f)
	return True

def loginpass():
	print("Login")
	counter = 1
	nama = input("Name : ")
	sandi = input("Password : ")
	checking = False
	passlog = False
	print("Checking name and password ...")
	sleep(2)
	if nama in user:
		checking = True
		passlog = (user[nama] == password)
	else:
		return False
