import pygame 
# dont know if this is nessasary 
from text_display import Text_Display 

class Quest():

	def __init__(self, npc_type, complete = False):
		self.npc_type 	= npc_type
		self.complete	= False

		self.speakables = []

		self.has_beer	= False

		if npc_type == "girl":
			self.quest_1()
		elif npc_type == "bartender":
			self.bartender()

	def quest_1(self):
		self.speakables = [
				"This Drink Tastes Gross"
		] 

	def bartender(self):
		self.speakables = [
		"What'll it be?"
		]