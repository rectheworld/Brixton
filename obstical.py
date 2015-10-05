import pygame 
import pygame.sprite 

def load_image(filename):
	return pygame.image.load(filename).convert()

class Obstical(pygame.sprite.Sprite):

	def __init__(self, obstical_type , file_path, inital_postion):
		pygame.sprite.Sprite.__init__(self)
		#A string delcaring the type of obstical ie "Table", "Bar"
		self.obstical_type 	= obstical_type 
		self.file_path		= file_path 
		self.inital_postion = inital_postion
		self.image 			= load_image(self.file_path)
		self.rect			= self.image.get_rect()
		self.rect.x 		= inital_postion[0]
		self.rect.y			= inital_postion[1]

