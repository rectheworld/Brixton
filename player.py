import os
import pygame 
import pygame.sprite
from animation import * 

class Player(pygame.sprite.Sprite):
	"""
	Player Class. Creates a sprite that can be moved by the player 

	Parameters
	----------
	inital_postion: A tuple in pixals representing where what play
		 should first appaear on the screen 

	fps: "Frams per Second". The speed at which the animation should 
		run

	"""
	# Import Spritesheet 
	spritesheet = Spritesheet("images/boy.png")

	#Directions 
	NORTH = 0 
	EAST  = 1
	SOUTH = 2
	WEST  = 3 

	# Define the Animations 
	STAND = 'stand'
	WALK = 'walk'

	def __init__(self, inital_postion, fps = 15):
		# inital the Super class of Sprite 
		pygame.sprite.Sprite.__init__(self)
		self.position = inital_postion
		self.rect = pygame.Rect(self.position[0], self.position[1], 48, 48)


		self.animations = {
		'stand' : [
			Animation(Player.spritesheet, fps, [(0,   7, 32, 48),]),
            Animation(Player.spritesheet, fps, [(0,  55, 32, 48),]),
            Animation(Player.spritesheet, fps, [(0, 102, 32, 48),]),
            Animation(Player.spritesheet, fps, [(0, 151, 32, 48),]),
		],

		'walk' : [
			Animation(Player.spritesheet, fps, [(0,   7, 32, 48), (36,   7, 32, 48), (73,   7, 32, 48)]),
            Animation(Player.spritesheet, fps, [(0,  55, 32, 48), (36,  55, 32, 48), (73,  55, 32, 48)]),
            Animation(Player.spritesheet, fps, [(0, 102, 32, 48), (36, 102, 32, 48), (73, 102, 32, 48)]),
            Animation(Player.spritesheet, fps, [(0, 151, 32, 48), (36, 151, 32, 48), (73, 151, 32, 48)]),
		],

		}


		self.direction = Player.EAST
		self.animation = Player.STAND


	def update(self):
		"""
		Creates the animation of the player walking.

		Called in process_events in main 
		""" 
		animation = self.animations[self.animation][self.direction]
		animation.updates(pygame.time.get_ticks())
		self.image = animation.frame
		self.rect = animation.rect
		self.rect.x = self.position[0]
		self.rect.y = self.position[1]
