import pygame
from spritesheet import *

class Animation: 
	def __init__(self, spritesheet, fps, rects, increment = 1):
		self.rects 			= rects
		self.increment		= increment
		self.current_frame	= 0
		self.delay			= 1000 / fps 
		self.last_update 	= 0 
		self.frames			= spritesheet.imgstat(self.rects, -1)
		self.frame 			= self.frames[self.current_frame]
		self.rect 			= pygame.Rect(self.rects[self.current_frame])


	def updates(self, current_time):
		# If the delay has passed, 
		if current_time - self.last_update > self.delay:
			self.last_update		= current_time
			self.current_frame		= (self.current_frame + 1) % len(self.frames)
			self.frame 				= self.frames[self.current_frame]
			self.rect 				= pygame.Rect(self.rects[self.current_frame])

