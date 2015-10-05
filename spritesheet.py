import os
import pygame


def load_image(filename):
	return pygame.image.load(filename).convert()

class Spritesheet:
	def __init__(self, filename):
		self.sheet = load_image(filename)


	def imgat(self, rect, colorkey = None):
		rect = pygame.Rect(rect)
		# Create a Pygame Surface for the Imgage of the Player 
		image = pygame.Surface(rect.size).convert()
		# Blit the image of the player to the sheet 
		image.blit(self.sheet, (0,0), rect)

		if colorkey is not None:
			if colorkey is -1:
				# Get the color of the pixal at location (0,0)
				colorkey = image.get_at((0,0))
			# Make the color of the colorkey transparent 
			image.set_colorkey(colorkey, pygame.RLEACCEL)
		return image

	def imgstat(self, rects, colorkey = None):
		# I think this function is used to clean frams for animation 
		imgs = []
		for rect in rects:
			imgs.append(self.imgat(rect, colorkey))
		return imgs 

