import pygame


class Settings:

	def __init__(self):
		self.screen_width = 800
		self.screen_height = 500
		self.title = "Alien Game"
		#self.bg_color = [230,230,230]
		animation_increment = 10
		self.bg_image = pygame.image.load('img/angkasa.jpg')