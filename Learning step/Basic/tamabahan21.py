from datetime import datetime

time = datetime.now()

print(time)
nama = input("PLease enter your name : ")
urutan = int(input("Please enter you queue number : "))


acc = ("%s%02d%2d%03s" % (time.year, time.month, time.day, urutan)

print(acc + nama)