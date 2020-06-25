from datetime import datetime

time = datetime.now()

print(time.day, time.hour, time.minute, time.second)
nama = input("PLease enter your name : ")
urutan = int(input("Please enter you queue number : "))
iD = ("%s%02d%2d%03s" % (time.year, time.month, time.day, urutan)
print(iD)