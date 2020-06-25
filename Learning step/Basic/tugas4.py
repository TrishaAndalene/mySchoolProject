from datetime import datetime 

passcode = 280506

print(datetime.now())
user = input("Officer name : ")
password = input("Enter the passcode : ")
if password != passcode :
	print("Wrong passcode..")
	print("Please ask the concerned officer or retry")
	password = input("Enter the passcode : ")

print("Welcome", user)
section = input("Please input your section : ") #section = jenis pekerjaan
urutan = int(input("Please input your queue number : "))
time = datetime.now()
ID = "%s%02d%2d%03s" % (time.year, time.month, time.day, urutan)
print("This is your number id : ", ID)