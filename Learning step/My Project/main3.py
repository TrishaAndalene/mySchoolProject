import fiturmain3
from time import sleep
from json import load, dump
from os import system

"""
usernametersimpan = "User"
passwordtersimpan = "123456"
usernameyangdimasukkan = input("Enter username :")
passwordyangdimasukkan = input("Enter password :")

"""

exist = fiturmain3.loadDat()

if exist:
	fiturmain3.passlog()
	print("Preparing machine ...")
	sleep(2)
	system('cls')
	print("Unpacking items .")
	sleep(0.5)
	system('cls')
	print("Unpacking items .. ")
	sleep(0.5)
	system('cls')
	print("Unpacking items ...")
	sleep(1)
	system('cls')
	print("Finishing machine ... ")








"""
while passwordyangdimasukkan != passwordtersimpan or usernameyangdimasukkan != usernametersimpan :
	print("The username or the password isn't true")

	usernameyangdimasukkan = input("Enter username :")
	passwordyangdimasukkan = input("Enter password :")



def _main_lobby():
	if usernameyangdimasukkan == usernametersimpan and passwordyangdimasukkan == passwordtersimpan :
		fiturmain3._main_lobby()
	print("Welcome back User :) \n")
	print("I'm your assistant")
	print("I will help you to use this project")
	print("So, Let's start!")
	input("Press the [enter] button to start..")


userInput ="0"
while userInput != "E":
	fiturmain3._main_page()
	userInput = input("Choose a number : ")
	if userInput == "1":
		print("Welcome to the Notes Writer")
		fiturmain3._main_menu1()
		userInput2 = "0"
		while userInput2 != "4":
			fiturmain3._main_menu1()
			userInput2 = input("You choose : ")
			if userInput2 == "1":
				fiturmain3._buat_catatan()
			if userInput2 == "2":
				fiturmain3._lihat_catatan()
			if userInput2 == "4":
				print("Thank you for trying Notes Writer")
				time.sleep(1.5)
				fiturmain3._main_page()

	if userInput == "2":
		fiturmain3._kalkulator_ling()
	if userInput == "3":
		fiturmain3._kalk_segi3()
	if userInput == "4":
		fiturmain3._kalk_petak()
if userInput == "E":
	print("Thank you for trying our Project")


"""


