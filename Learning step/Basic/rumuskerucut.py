import math

#Program dibuat oleh unknown
print("Menghitung luas permukaan bola")
jarijari = float(input("Masukkan nilai jari-jari = ..."))
garispelukis = float(input("Masukkan nilai garis pelukis = ..."))
luaspermukaan = ((math.pi*(jarijari*jarijari) + (math.pi*(garispelukis*jarijari))))
tinggi = (math.sqrt(garispelukis**2-jarijari**2))
volume = (math.pi*jarijari*jarijari*jarijari*tinggi)
print(f"Luas permukaan = {luaspermukaan}")
print(f"Volume = {volume}")