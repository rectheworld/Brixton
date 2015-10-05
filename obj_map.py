import pygame 
from obstical import Obstical

class Obj_Map():
	"""
	This class will creat obstical objects and store their 
	location. The Floor will also be drawn with this class 
	"""

	def __init__(self):

		self.sprite_obstical_list 	= pygame.sprite.Group()
		self.obstical_list = []

		self.table 			= Obstical("table", "images/table.png", (48 * 3,48 * 4))

		self.obstical_list.append(self.table)

		self.sprite_obstical_list.add(self.table)



	def render_map():
		pass 







