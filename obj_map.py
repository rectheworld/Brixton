import pygame 
from obstical import Obstical
from npc import NPC
from spritesheet import Spritesheet 

tile_size = 48
class Obj_Map():
	"""
	This class will creat obstical objects and store their 
	location. The Floor will also be drawn with this class 
	"""

	def __init__(self):

		self.sprite_obstical_list 	= pygame.sprite.Group()
		self.obstical_list 			= []
		self.npc_list				= [] 
		# Create Obbjects
		#Bathrooms
		self.table1 			= Obstical("table", "images/table.png", [tile_size * (11 - 1),tile_size * (4 -1)])
		self.table2 			= Obstical("table", "images/table.png", [tile_size * (11 -1),tile_size * (6 -1)])
		self.table3 			= Obstical("table", "images/table.png", [tile_size * (11 -1),tile_size * (8 - 1)])

		# Bathrooms 
		# Will not be added to sprite list because player can walk up to them 
		self.mens_room			= Obstical("mens_room", "images/mens_bathroom.png", [tile_size * (11 -1), tile_size * (1 - 1)])
		self.womens_room		= Obstical("womens_room", "images/womens_bathroom.png", [tile_size * (12 -1), tile_size * (1 - 1)])

		# Patio Bar 
		self.patio_bar1 		= Obstical("patio_bar", "images/patio_bar.png", [tile_size * (13 - 1), tile_size * (1 - 1)])
		self.patio_pillar2		= Obstical("patio_pillar", "images/patio_pillar.png", [tile_size * (13 - 1), tile_size * (2 - 1)])
		self.patio_bar3			= Obstical("patio_bar", "images/patio_bar.png", [tile_size * (13 - 1), tile_size * (3 - 1)])
		self.patio_bar4			= Obstical("patio_bar", "images/patio_bar.png", [tile_size * (13 - 1), tile_size * (4 - 1)])
		self.patio_pillar5		= Obstical("patio_pillar", "images/patio_pillar.png", [tile_size * (13 - 1), tile_size * (5 - 1)])
		self.patio_bar6			= Obstical("patio_bar", "images/patio_bar.png", [tile_size * (13 - 1), tile_size * (6 - 1)])
		self.patio_bar7			= Obstical("patio_bar", "images/patio_bar.png", [tile_size * (13 - 1), tile_size * (7 - 1)])
		self.patio_pillar8		= Obstical("patio_pillar", "images/patio_pillar.png", [tile_size * (13 - 1), tile_size * ( 8- 1)])
		self.patio_bar9			= Obstical("patio_bar", "images/patio_bar.png", [tile_size * (13 - 1), tile_size * (9 - 1)])
		self.patio_bar10 		= Obstical("patio_bar", "images/patio_bar.png", [tile_size * (13 - 1), tile_size * (10 - 1)])

		# Ceiling 				
		self.ceiling1			= Obstical("ceiling", "images/ceiling.png", [tile_size * (14 - 1), tile_size * (1 - 1)])
		self.ceiling2			= Obstical("ceiling", "images/ceiling.png", [tile_size * (14 - 1), tile_size * (2 - 1)])
		self.ceiling3			= Obstical("ceiling", "images/ceiling.png", [tile_size * (14 - 1), tile_size * (3 - 1)])
		self.ceiling4			= Obstical("ceiling", "images/ceiling.png", [tile_size * (14 - 1), tile_size * (4 - 1)])
		self.ceiling5			= Obstical("ceiling", "images/ceiling.png", [tile_size * (14 - 1), tile_size * (5 - 1)])
		self.ceiling6			= Obstical("ceiling", "images/ceiling.png", [tile_size * (14 - 1), tile_size * (6 - 1)])
		self.ceiling7			= Obstical("ceiling", "images/ceiling.png", [tile_size * (14 - 1), tile_size * (7 - 1)])
		self.ceiling8			= Obstical("ceiling", "images/ceiling.png", [tile_size * (14 - 1), tile_size * (8 - 1)])
		self.ceiling9			= Obstical("ceiling", "images/ceiling.png", [tile_size * (14 - 1), tile_size * (9 - 1)])
		self.ceiling10			= Obstical("ceiling", "images/ceiling.png", [tile_size * (14 - 1), tile_size * (10 - 1)])

		# Long Table 
		self.long_table			= Obstical("long_table", "images/long_table.png", [tile_size * (6 - 1), tile_size * (6 -1)])

		# Bar
		self.bar			= Obstical("bar", "images/bar_front.png", [tile_size * (2 - 1), tile_size * (2 -1)])
		self.bar_left		= Obstical("bar_left", "images/bar_left.png", [tile_size * (2 - 1), tile_size * (2 -1)])
		self.bar_right		= Obstical("bar_right", "images/bar_right.png", [tile_size * (9 - 1), tile_size * (2 -1)])		

		# DJ botth 
		self.dj_booth		= Obstical("dj_booth", "images/dj_booth.png", [tile_size * (2 - 1), tile_size * (9 -1)])

		# Exit 
		self.exit_door		= Obstical("exit_door", "images/exit.png", [tile_size * (1 - 1), tile_size * (4 -1)])		
		

		####################
		#CREATE SOME NPCS
		####################

		# Create a girl
		self.girl1 			= NPC("girl", "images/girl.png", [tile_size * (7 - 1), tile_size * (7 -1)])

		
		# Add objects to a list of obsticals 
		self.obstical_list.append(self.table1)
		self.obstical_list.append(self.table2)
		self.obstical_list.append(self.table3)

		self.obstical_list.append(self.mens_room)
		self.obstical_list.append(self.womens_room)

		self.obstical_list.append(self.patio_bar1)
		self.obstical_list.append(self.patio_pillar2)
		self.obstical_list.append(self.patio_bar3)
		self.obstical_list.append(self.patio_bar4)
		self.obstical_list.append(self.patio_pillar5)
		self.obstical_list.append(self.patio_bar6)
		self.obstical_list.append(self.patio_bar7)
		self.obstical_list.append(self.patio_pillar8)
		self.obstical_list.append(self.patio_bar9)
		self.obstical_list.append(self.patio_bar10)

		self.obstical_list.append(self.ceiling1)
		self.obstical_list.append(self.ceiling2)
		self.obstical_list.append(self.ceiling3)
		self.obstical_list.append(self.ceiling4)
		self.obstical_list.append(self.ceiling5)
		self.obstical_list.append(self.ceiling6)
		self.obstical_list.append(self.ceiling7)
		self.obstical_list.append(self.ceiling8)
		self.obstical_list.append(self.ceiling9)
		self.obstical_list.append(self.ceiling10)

		self.obstical_list.append(self.long_table)

		self.obstical_list.append(self.bar)
		self.obstical_list.append(self.bar_left)
		self.obstical_list.append(self.bar_right)

		self.obstical_list.append(self.dj_booth)

		self.obstical_list.append(self.exit_door)

		# Add npcs to npc list 
		self.npc_list.append(self.girl1)


		# Make the collison rects for the table a little bit smaller than 48 x 48 so the 
		# layer can walk between the tables and in front of them
		# Ie the collision rect only covers to top semi circle of the table 
		# Bar needs to be adjusted too 
		for obj in self.obstical_list:
			if obj.obstical_type == "table":
				obj.rect = (obj.inital_postion[0] + 7, obj.inital_postion[1] + 7, 34, 10) 
			elif obj.obstical_type == "long_table":
				obj.rect = (obj.inital_postion[0] + 7, obj.inital_postion[1] + 7, 34, 154) 
			elif obj.obstical_type== "bar":
				obj.rect = (obj.inital_postion[0] + 5, obj.inital_postion[1] + tile_size - 5, (tile_size * 8) - 5, tile_size - 25)				



		# add objects to a sprite list to check for colision 
		self.sprite_obstical_list.add(self.table1)
		self.sprite_obstical_list.add(self.table2)
		self.sprite_obstical_list.add(self.table3)

		self.sprite_obstical_list.add(self.patio_bar1)
		self.sprite_obstical_list.add(self.patio_pillar2)
		self.sprite_obstical_list.add(self.patio_bar3)
		self.sprite_obstical_list.add(self.patio_bar4)
		self.sprite_obstical_list.add(self.patio_pillar5)
		self.sprite_obstical_list.add(self.patio_bar6)
		self.sprite_obstical_list.add(self.patio_bar7)
		self.sprite_obstical_list.add(self.patio_pillar8)
		self.sprite_obstical_list.add(self.patio_bar9)
		self.sprite_obstical_list.add(self.patio_bar10)

		self.sprite_obstical_list.add(self.long_table)

		self.sprite_obstical_list.add(self.bar)
		self.sprite_obstical_list.add(self.bar_left)
		self.sprite_obstical_list.add(self.bar_right)

		self.sprite_obstical_list.add(self.dj_booth)

		self.sprite_obstical_list.add(self.girl1)


	def render_map():
		pass 







