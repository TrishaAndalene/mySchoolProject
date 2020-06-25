from os import system

nama = [['Sally', '564738'], ['Jeff', '102938'], ['William', '1357246']]
ops = '0'
loginpass = False
crash = False

def login():
	print("Please complete this identification!")
	user = input("Name : ")
	password = input("Password : ")
	for data in nama:
		if data[1]== password and data[0] == user:
			print("Welcome back to Length converter,", user)
			return True
	else:
		print("There's no name and password like that")
		input("[ENTER] to retry")
		return False


def main_menu():
	print("Please input your option")
	print("[1] from Centimetre to metre and milimetre")
	print("[2] from Metre to kilometre and centimetre")
	print("[3] from kilometre to metre")
	print("[E] Exit converter")


def cm():
	print("Option number 1")
	x = int(input("Please input the length: "))
	m1 = x/100
	print("Length in metre : %.1f metre" % (m1))
	mm1 = x*10
	print("Length in milimetre : %.1f milimetre" % (mm1))


def m():
	print("Option number 2")
	x = int(input("Please input the length : "))
	km1 = x/1000
	print("Length in kilometre : %.2f kilometre" % (km1))
	cm1 = x*100
	print("Length in centimetre : %.2f centimetre" % (cm1))


def km():
	print("Option number 3")
	x = int(input("Please input the length : "))
	m2 = x*1000
	print("Length in metre : %.1f metre" % (m2))


while not loginpass:
	system('cls')
	loginpass = login()


else:
	input("Press [ENTER] to continue")
	

while not crash:
	system('cls')
	main_menu()
	ops = input("Option : ")

	if ops == 'E':
		crash = True
		print("Thankyou for trying")
	if ops == '1':
		system('cls')
		cm()
		input("Press [ENTER] to go back to the menu")
	if ops == '2':
		system('cls')
		m()
		input("Press [ENTER] to go back to the menu")
	if ops == '3':
		system('cls')
		km()
		input("Press [ENTER] to go back to the menu")





