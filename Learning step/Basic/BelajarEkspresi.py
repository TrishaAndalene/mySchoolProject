ongkos = float(input("Duitnyo brapo? "))

if ongkos > 15000:
	print("Kamu dapet tiket jalan-jalan keliling dunia, tapi bayar sendiri, ya.")
elif ongkos > 99 :
	print("Kamu sudah kaya gk perlu hadiah.")
elif ongkos < 10 :
	print("Kamu dapet tiket pesawat, tapi bayar sendiri.")
else :
	print("Kamu dapet rumah mansion baru di manapun.")
