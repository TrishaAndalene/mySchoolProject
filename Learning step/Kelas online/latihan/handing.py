#Topic : handling Error silently (No crash apps)
# with Try, Except, Else, and Finally

"""
Cara pertama:

try: #coba pertama kali                        --------
	usia = int(input('Usia kamu ? ')) #integer        |
 	                                              #   |
except ValueError: #kalau salah                   #   |
	Msg = 'Invalid input, Please ener real number'#   |
	print(msg)                                    #   |---- cuman sekali
	                                              #   |
else: #kalau sudah benar                              |
	print(usia)                                   #   |
	                                              #   |
finally: #ending jadi kalo salah atau benar tetap ada |
	print('Program is running well')            # -----
"""

"""
Cara ke-2:

usia = 0 #                              ----------|
#                                                 |
#                                                 |
def cekUsia():#                                   |
	global usia#                                  |
	try:#                                         |
		usia = int(input("Input your name : "))#  |
#                                                 |
	except ValueError:#                           |
		print("Please answer correctly ...")#     |
		return False#                             |---- kalo mau nambah "Finally" ngak pengaruh karna cuman endingnya aja
#                                                 |
	else:#                                        |
		return True#                              |
#                                                 |
#                                                 |
number = False#                                   |
#                                                 |
#                                                 |
while not number:#                                |
	number = cekUsia()#                           |
else:#                                            |
	print(usia)#                       -----------|
"""

#Latihan 1

from json import load, dump
from os import system
from time import sleep

filename = ''
contents = []

system('cls')

def checkfile():
	global filename, contents
	system('cls')
	filename = input("Input your file : ")
	filename += '.json'

	try:
		with open(filename) as file:
			contents = load(file)

	except FileNotFoundError:
		print(f"File {filename} doesn't exist ..")
		input("[Enter] to retry")
		return False

	else:
		return True

exist = False #kalo existnya true jd 'while exist'

while not exist:
	exist = checkfile()
else:
	print('Rebooting system ...')
	sleep(2)
	system('cls')
	print('Unpacking items ...')
	sleep(2)
	system('cls')
	print('Loading ...')
	sleep(2)
	system('cls')
	print(f"Source : {filename}")
	print('Welcome back :)')

