import sys
import pygame

from settings import Settings
from ship import Ship

#my_image = pygame.image.load('angkasa.JPG')

class AlienGame:

	def __init__(self):
		#start pygame
		pygame.init()
		self.game_setting = Settings()

		self.screen = pygame.display.set_mode([self.game_setting.screen_width, self.game_setting.screen_height])
		self.title = pygame.display.set_caption(self.game_setting.title)
		#self.bg_color = self.game_setting.bg_color #RGB
		self.bg_image = self.game_setting.bg_image

		self.game_ship = Ship(self)


	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			#self.screen.fill(self.bg_color)

			self.screen.blit(self.bg_image, (0,0))
			self.game_ship.blitme()
			pygame.display.flip() #method agar frame dalam game berjalan


if __name__ == "__main__": #expression (true/false)
	theGame = AlienGame() #assignment (pengisian memori)
	theGame.run_game()

#variabel -> attribute
#function -> method