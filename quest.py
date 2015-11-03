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

		self.speak_index = 0
		self.speak = self.speakables[self.speak_index]

	def quest_1(self):
		self.speakables = [
				"This Drink Tastes Gross",
				"Why are you still here?"
		] 

	def bartender(self):
		self.speakables = [
		"Heres a Beer"
		]

	def progress_quest(self):
		print self.speak_index, len(self.speakables)
		if self.speak_index < len(self.speakables) - 1:
			self.speak_index += 1
			self.speak = self.speakables[self.speak_index]
			print self.speak 
			return self.speak
			