import math

#program dibuat oleh Unknown
print("Program menghitung akar akar PK")
a = float(input("Masukan koefisien xKuadrat : "))
b = float(input("Masukan koefisien x : ")) 
c = float(input("Masukan konstanta : "))

diskriminan = b**2-4*a*c
x1 = (-b+math.sqrt(diskriminan))/2*a
x2 = (-b-math.sqrt(diskriminan))/2*a
print(f"X1 = {x1}")
print(f"X2 = {x2}")
