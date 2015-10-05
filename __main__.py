import pygame
from pygame import *


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

		# Used in Process Events
		self.old_keys		= {} 

		from player import Player
		self.player			= Player([48,48])

	# Used to create easy movment , called in process events 
	def difference(self, tuple_1, tuple_2):
		results = []
		for i in range(len(tuple_1)): results.append(tuple_1[i] and not tuple_2[i])
		return tuple(results)


	#Think ( A Little bit a Listen)
	def process_events(self):
		#Collect the Keystrocks 
		walk = False 
		old_pos = (self.player.position[0], self.player.position[1])

		keys = pygame.key.get_pressed()

		# Not toally sure what this code does 
		if self.old_keys:
			self.difference(keys, self.old_keys)
			self.difference(self.old_keys, keys)
		self.old_keys = keys 

		if keys[K_LEFT]:
			if self.player.position[0] > 0:
				self.player.position[0] -= 1 
			self.player.direction = self.player.WEST
			self.player.animation = self.player.WALK 
			walk = True 

		if keys[K_RIGHT]:
			self.player.position[0] += 1
			self.player.direction = self.player.EAST
			self.player.animation = self.player.WALK
			walk = True

		if keys[K_UP]:
			if self.player.position[1] > 0:  
				self.player.position[1] -= 1
			self.player.direction = self.player.NORTH
			self.player.animation = self.player.WALK
			walk = True

		if keys[K_DOWN]:
			self.player.position[1] += 1 
			self.player.direction = self.player.SOUTH
			self.player.animation = self.player.WALK
			walk = True

		if not walk:
			self.player.animation = self.player.STAND

		#Update Player Variables 
		self.player.update() 




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
			self.process_events()


			self.render()

			self.clock.tick(60)

			pygame.display.flip()


if __name__== "__main__":
	game = Game()
	game.main()