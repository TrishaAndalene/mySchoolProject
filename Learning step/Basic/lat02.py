"""
Nama Pembuat : Trisha andalene
Tanggal Dibuat : 11 Januari 2020
Nama Program : Belanja di Minimarket
"""

#Pelanggan = "Devan & Nico"
Pelanggan = input("Masukkan nama Pelanggan")
UangDiDompet = int(input(f"uangnya ada berapa {Pelanggan} ?"))

print("PT. Minimarket Mania")
print("Selamat berbelanja....")
print("Nama Pelanggan : ",Pelanggan,"\n")


Chitato = 12000
Fanta = 15000
Gas = 25000
FiestaNugget = 45000
Indomie = 2500
Oreo = 8000
Campina = 27000
Pulsa = 100000

totalBelanjaan = 2*Chitato + Fanta + Gas + FiestaNugget + 10*Indomie + 3*Oreo + Campina + Pulsa
print("Total :", totalBelanjaan)
pajak = 0.1*totalBelanjaan
print("Pajak : ", pajak)
totalBelanjaan += pajak
print("Yang harus dibayar : ", totalBelanjaan)
UangDiDompet -= totalBelanjaan
print("Kembalian : ", UangDiDompet,"\n")
print("Terimakasih telah berbelanja")
