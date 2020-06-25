#alien game
import sys
import pygame

from setting import Settings
from ship import Ship

class AlienGame:
	#semua pengaturan aset dan behavior game
	def __init__(self):
		#memulai game dengan sumber modul / library dari pygame
		pygame.init()
		self.game_setting = Settings()
		self.screen = pygame.display.set_mode([self.game_setting.screen_width, self.game_setting.screen_height])
		self.title_game = 'Alien Shooter'
		pygame.display.set_caption(self.title_game)

		self.ship = Ship(self)
		


	def run_game(self):
		#memulai game dengan looping. diset infinite loop
		while True:
			#melihat kejadian yang ada di dalam game
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()


			self.screen.fill(self.game_setting.bg_color)
			self.ship.blitme()

			#menampilkan kejadian di layar
			pygame.display.flip()


if __name__ == "__main__": #__name__ itu sama seperti 'init'(sudah ada variabel(special)) dan kalo 'main' itu berarti kita bukak pakai file py yang sama. Jadi kalau beda file tidak pakai main
	AG = AlienGame()
	AG.run_game()




