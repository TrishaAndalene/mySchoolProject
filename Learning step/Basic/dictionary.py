BukuTelepon = {
	"Sally" : "0812123123",
	"Nightmare" : "089600112233",

}

#print(BukuTelepon[input("Masukkan nama yang akan ditelepon : ")])
BukuTelepon["Ticci Toby"] = input("Masukkan nomor telepon : ")
print(BukuTelepon)
for item in BukuTelepon:
	print(item)
#dictionary ada 2 :
#index
#value