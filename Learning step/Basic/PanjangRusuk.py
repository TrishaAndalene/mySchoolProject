import math

#program dibuat oleh Unknown
print("Program Hitung Panjang Diagonal Kubus")
rusuk = float(input("Masukan panjang rusuk ..."))
diagonalbidang = (math.sqrt(2*(rusuk**2)))
diagonalruang = (math.sqrt(diagonalbidang**2 + rusuk**2))
print(f"Diagonal bidang = {diagonalbidang}")
print(f"Diagonal ruang = {diagonalruang}")