# The Brixton:
# A Little Game about Finding Love
# Developer: Ren 
# Date: 10-05-2015


import pygame
from pygame import *
from npc import NPC 




FPS = 60
SCREEN_SIZE = (640, 480)


class Game(object):
	"""
	Main Game object of the Game. This class holds the 
	pygame screen and clock aspects. Infomation about the player is 
	imported into this class. 

	Parameters
	----------
	screen_size: A tuple object representing the size of the screen in 
		pixals (note: the order of the tuple is (y, x))

	fps: "Frames per Second". A number representing how often the game 
		screen should be refreshed 
	"""
	def __init__(self, screen_Size = SCREEN_SIZE, fps = FPS):
		pygame.init()
		
		
		self.screen_size 	= SCREEN_SIZE
		self.fps 			= fps 
		#Creates the Pygame Screen object 
		self.screen 		= pygame.display.set_mode(self.screen_size)

		# size of Exch tile in the grid
		self.tile_size		= 48

		# Creates the clock that allows to the game to be animated 
		self.clock 			= pygame.time.Clock()
		
		# While this varable is true, the game will continue to Run 
		self.running		= True

		# Used in Process Events
		self.old_keys		= {} 

		self.floor_tile		= pygame.image.load("images/wood.png").convert()
		from player import Player
		self.player			= Player([self.tile_size  * 6, self.tile_size * 4])

		from obj_map import Obj_Map
		self.obj_map 			= Obj_Map()

		# this is text that is spoken at the next render 
		self.interaction	= False
		self.npc_active		= None 

		self.speech_box		= pygame.image.load("images/text_box.png").convert()
		self.speech_box.set_colorkey((255,255,255), pygame.RLEACCEL)

	def difference(self, tuple_1, tuple_2):
		"""
		Used to create smooth animation movement 

		Parameters
		----------
		tuple_1: A tuple of two keys  
		tuple_2: A tuple of two keys  

		"""
		results = []
		for i in range(len(tuple_1)): results.append(tuple_1[i] and not tuple_2[i])
		return tuple(results)


	#Think ( A Little bit a Listen)
	def process_events(self):
		"""
		This is the "Think" portion of the game loop.
		It process the keystrocks the player makes and updates the 
		player's infomation 

		Parameters
		----------
		None:

		This function is called in the main() function 
		"""

		#Collect the Keystrocks 
		walk = False 
		old_pos = [self.player.position[0], self.player.position[1]]

		keys = pygame.key.get_pressed()

		# Not toally sure what this code does 
		if self.old_keys:
			self.difference(keys, self.old_keys)
			self.difference(self.old_keys, keys)
		self.old_keys = keys 

		# Test if the a directional key is pressed,
		# if it is, move and animate the character 
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

		if keys[K_x]:
			for npc in self.obj_map.npc_list:
				if pygame.sprite.collide_circle(self.player, npc):
					self.interaction	 = True
					self.npc_active 	 = npc 
					npc.turn_towards_player(self.player.position)
					self.speak_next = npc.speak.label



		if not walk:
			self.player.animation = self.player.STAND
		if walk:
			#Just going to hijack this function 
			if self.npc_active != None: 
				self.npc_active.turn_towards_player((self.npc_active.position[0], self.npc_active.position[1] + 10))

				# You've just talked to an NPC, the next line of code advances the speak she says to you 
				self.npc_active.action_advance()
			self.interaction	 = False
			self.npc_active		= None 

		self.player.rect.x = self.player.position[0]
		self.player.rect.y = self.player.position[1]

		
		collosion_list = pygame.sprite.spritecollide(self.player, self.obj_map.sprite_obstical_list, False)

		if len(collosion_list) > 0:
			 self.player.position = old_pos

		#Update Player Variables 

		self.player.update() 
 	
	def render(self):
		"""
		This is the main "Speak" feature of the game. 
		it draaws the player, map, npc's to the screen

		Parameters
		----------
		None

		This function is called in the main function 
		"""

		# Render the Floor 
		
		col = 0 
		while col <= self.screen_size[0]:
			row = 0
			while row <= self.screen_size[1]:
				self.screen.blit(self.floor_tile, (col, row))
				row += self.tile_size
			col += self.tile_size

		#Render the Obsticals 
		for obj in self.obj_map.obstical_list:
			self.screen.blit(obj.image, obj.inital_postion)

		# Render the npcs 
		for npc in self.obj_map.npc_list:
			self.screen.blit(npc.image, npc.position)


		# render the player 
		self.screen.blit(self.player.image, self.player.position)

	def main(self):
		"""
		This is the main game loop of the game. 
		It will run continiously until the player closes the screen 

		Parameters
		----------
		None 

		"""

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

			if self.interaction == True:
				#pygame.draw.rect(self.screen, (255,255,255),(100,100, 100, 50))
				self.screen.blit(self.speech_box, (200,400))
				self.screen.blit(self.npc_active.speak.label, (240,420))

			self.clock.tick(60)

			pygame.display.flip()


if __name__== "__main__":
	game = Game()
	game.main()