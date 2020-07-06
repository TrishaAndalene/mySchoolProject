import pygame

class Ship:

	def __init__(self, info_game):

		self.screen = info_game.screen
		self.screen_rect = info_game.screen.get_rect()

		self.image = pygame.image.load("img/putih.PNG")
		self.rect = self.image.get_rect()

		self.rect_midbottom = self.screen_rect.midbottom

	def blitme(self):
		self.screen.blit(self.image, self.rect)