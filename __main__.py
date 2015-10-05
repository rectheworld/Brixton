import pygame


FPS = 60
SCREEN_SIZE = (640, 480)


class Game(object):

	def __init__(self, screen_Size = SCREEN_SIZE, fps = FPS):
		pygame.init()
		
		
		self.screen_size 	= SCREEN_SIZE
		self.fps 			= fps 
		self.screen 		= pygame.display.set_mode(self.screen_size)
		self.clock 			= pygame.time.Clock()
		self.running		= True

		from player import Player
		self.player			= Player((48,48))

	#Think ( A Little bit a Listen)
	def process_events(self):




	# Speak 	
	def render(self):
		self.screen.blit(self.player.image, self.player.position)


	def main(self):
		# Main Game Loop 

		while self.running: 

			events = pygame.event.get()

			# Listen for an Exit 
			for event in events: 
				if event.type == pygame.QUIT:
					self.running = False
					pygame.quit()  


			self.screen.fill((255,255,255))

			# this should go into a Process events function 
			self.player.update()


			self.render()

			pygame.display.flip()


if __name__== "__main__":
	game = Game()
	game.main()