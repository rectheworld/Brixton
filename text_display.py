import pygame 

class Text_Display(object):


	def __init__(self, text):
		self.font		= pygame.font.SysFont("monospace", 15)
		self.text 		= text 
		self.label		= self.font.render(self.text, 1, (255, 255,0))
		self.rect		= pygame.Rect(50,200, 450, 50)

