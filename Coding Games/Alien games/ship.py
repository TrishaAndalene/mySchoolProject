import pygame

class Ship:

	def __init__(self, game):
		#menginisiasi pesawat luar angkasa


		#memulai posisi sesuai dengan besar layar game
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect() 


		#memasukkan gambar pesawat
		self.image = pygame.image.load('img/kapal2.png') #img = nama folder yang ada gambar kapalnya
		self.rect = self.image.get_rect()


		#mengatur posisi dari pesawat -> menyamakan koordinat atau posisi dari kapal
		self.rect.leftbottom = self.screen_rect.leftbottom


	def blitme(self):
		#untuk menampilkan kapal untuk setiap frame dalam game
		self.screen.blit(self.image, self.rect) #image baris 13, rect baris 14, tapi dieditnya di baris 17