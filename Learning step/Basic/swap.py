a = float(input("Masukkan nilai a : "))
b = float(input("Masukkan nilai b : "))
print("a = ",a)
print("b = ",b)
b += a
a = b - a
b -= a

print("maka a = ",a)
print("maka b = ",b)