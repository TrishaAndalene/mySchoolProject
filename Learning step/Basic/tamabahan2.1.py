from datetime import datetime

nama = input("PLease enter your name : ")
urutan = int(input("Please enter you queue number : "))

time = datetime.now()

ID = ("%s%2d%2d%03d-" % (time.year, time.month, time.day, urutan, nama))

print("This is your id number : ", ID)