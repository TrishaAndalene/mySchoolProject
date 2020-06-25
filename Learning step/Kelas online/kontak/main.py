from json import load, dump
from datetime import datetime
from os import system
import feature
from time import sleep

time = datetime.now()
print("%s%02d%2d" % (time.year, time.month, time.day))

statusload = feature.loadstat()

if statusload : 
	feature.loginpass()
	print("Checking complete ...")
	sleep(2)
	print("Welcome")
	sleep(1.5)
	system('cls')
	print("Unpacking items ...")
	sleep(2)
	system('cls')
	print("Loading data ...")
	sleep(1.5)
	print("Loading complete")
	pilih = "0"
	feature.menu()

	while pilih != "Q":
		system('cls')
		feature.menu1()
		pilih = input("Option : ")
		if pilih == "1":
			feature.itemlist()
		elif pilih == "2":
			feature.add()
		elif pilih == "3":
			feature.rem()
		elif pilih == "4":
			feature.search()

	
	if pilih == "Q":
		print("Thank you for choosing our application :)")
			
else:
	print("Apps is not responding ..")




