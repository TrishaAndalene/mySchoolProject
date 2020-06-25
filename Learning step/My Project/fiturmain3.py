from os import system
from time import sleep
import math
from getpass import getpass
from json import load, dump
pi = 3.14

Data = {}

"""
def _main_lobby():
	os.system("cls")
	print("Welcome back User :) \n")
	print("I'm your assistant")
	print("I will help you to use this project")
	print("So, Let's start!")
	input("Press the [enter] button to start..")
"""

user = {}


def loadDat():

	global User, Data
	print("Loading ...")
	sleep(0.5)
	system('cls')

	with open('data1.json') as f:
		user = load(f)

	with open('data2.json') as f:
		Data = load(f)

	return True

def passlog():
	system('cls')
	print("Login : ")
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
		input("{Enter] to retry")
		system('cls')
		nama = input("Name : ")
		sandi = getpass("Password : ")
		print("Checking name and password ...")
		sleep(2)
		if nama in user:
			datacheck = True
			passlogin = (user[nama] == sandi)
	else:
		return True
	


def _main_page():
	os.system("cls")
	print("Welcome to the application list :)")
	print("So, at here you can choose one number")
	print("Please choose one of this application : \n")
	print("[1] Notes Writer ")
	print("[2] Circle Calculation ")
	print("[3] Triangle Calculation")
	print("[4] Square Calculation")
	print("[E] Exit the project ")

def _main_menu1():
	os.system("cls")
	print("Notes Writer \n")
	print("[1] Write Notes")
	print("[2] See Notes")
	print("[3] Delete Notes")
	print("[4] Exit ")

def _buat_catatan():
	os.system("cls")
	print("Write your notes here : \n")
	catatan = input()
	Data.append(catatan)
	print("Note saved")
	time.sleep(1.5)

def _lihat_catatan():
	os.system("cls")
	if len(Data) > 0:
		print("Saved Notes : ")
		for catatan in Data:
			print(catatan)
		input("Press [enter] to go to the menu")
	else:
		print("No notes saved yet")
		input("Press [enter] to go to the menu")

def _kalkulator_ling():
	os.system("cls")
	print("Welcome to the Circle Calculation")
	r = float(input("Enter the r : "))
	B = pi*(r**2)
	C = pi*2*r
	print("Circle area : ", B)
	print("Circle border :  ", C)
	print("Thank you for trying Circle Calculation")
	input("Press [enter] to go to the main menu")

def _kalk_segi3():
	os.system("cls")
	print("Welcome to the Triangle Calculation")
	a = float(input("Enter a : "))
	t = float(input("Enter t : "))
	b = (math.sqrt(a**2 + t**2))
	k = a + b + t
	l = (a*t)/2
	print("Triangle area : ", l)
	print("Triangle border : ", k)
	print("Thank you for trying the Triangle Calculation")
	input("Press [enter] to go to the main menu")

def _kalk_petak():
	os.system("cls")
	print("Welcome to the Square Calculation ")
	s = float(input("insert s : "))
	l = s**2
	k = 4*s
	print("Square area = ", l)
	print("Square border = ",k)
	input("Press [enter] to back to main menu")



"""
def _kalk_sect():
	os.system("cls")
	print("Calculation Section \n")
	print("[1] aritmathics")
	print("[2] Area ")
	print("[3] Border")
	print("[E] to exit the application")
	"""
"""
def _kalk_arit():
	os.system("cls")
	print("Aritmathics Section \n")
	print("Please pick a number : ")
	print("[1] Plus ")
	print("[2] Minus")
	print("[3] Division")
	print("[4] Times")
	print("[E] to exit Area Section ")
"""
"""
def _kalk_tam():
	os.system("cls")
	float(input("Please insert a : "))
	float(input("Please insert b : "))
	c = a + b
	print("The Result is : ", c)
	input("Press [enter] to go back to the Aritmathics Section")
"""

