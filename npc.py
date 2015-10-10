import pygame 
import pygame.sprite
from spritesheet import Spritesheet
from animation import Animation

def load_image(filename):
	return pygame.image.load(filename).convert()

class NPC(pygame.sprite.Sprite, Spritesheet):

	

			#Directions 
	NORTH = 3 
	EAST  = 2
	SOUTH = 0
	WEST  = 1 

	# Define the Animations 
	STAND = 'stand'
	WALK = 'walk'
	
	def __init__(self, obstical_type , file_path, inital_postion):
		pygame.sprite.Sprite.__init__(self)
		self.postion 		= inital_postion
		fps 				= 15 
		self.obstical_type 	= obstical_type
		self.file_path		= file_path
		self.spritesheet 	= Spritesheet(self.file_path)
		# Size of rect for the first girl i found, this might be a parameter later 
		self.rect = pygame.Rect(self.postion[0], self.postion[1], 40, 20)

		self.animations = {
		'stand' : [
			Animation(self.spritesheet, fps, [(50,   0, 48, 48),]),
            Animation(self.spritesheet, fps, [(50,  55, 32, 48),]),
            Animation(self.spritesheet, fps, [(50, 102, 32, 48),]),
            Animation(self.spritesheet, fps, [(50, 151, 32, 48),]),
		],

		'walk' : [
			Animation(self.spritesheet, fps, [(0,   7, 32, 48), (36,   7, 32, 48), (73,   7, 32, 48)]),
            Animation(self.spritesheet, fps, [(0,  55, 32, 48), (36,  55, 32, 48), (73,  55, 32, 48)]),
            Animation(self.spritesheet, fps, [(0, 102, 32, 48), (36, 102, 32, 48), (73, 102, 32, 48)]),
            Animation(self.spritesheet, fps, [(0, 151, 32, 48), (36, 151, 32, 48), (73, 151, 32, 48)]),
		],

		}

		self.direction = NPC.SOUTH
		self.animation = NPC.STAND

		animation = self.animations[self.animation][self.direction]
		animation.updates(pygame.time.get_ticks())
		self.image = animation.frame


		def update(self):
			"""
			Creates the animation of the npc occolating.

			Called in process_events in main 
			""" 
			animation = self.animations[self.animation][self.direction]
			animation.updates(pygame.time.get_ticks())
			self.image = animation.frame
			self.rect = animation.rect
			self.rect.x = self.position[0]
			self.rect.y = self.position[1]
