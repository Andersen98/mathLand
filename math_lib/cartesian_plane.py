import pygame

class Cartesian_Plane(object):

	def __init__(self, environment):
		"""Initialized plane, gets its state from the current environment"""
		self.environment = environment

	def update(self, environment):
		"""Udates plane with current environment"""
		self.environment = environment	
	
	def draw(self, ml_settings, screen):
		"""Draw plane to screen"""
		#origin
		origin_vect = self.environment.get_origin()
		#i vector given the new origin
		i_vect = self.environment.get_i_vect().add(origin_vect)
		

		pygame.draw.line(screen, ml_settings.cartesian_color, origin_vect.get_tuple() , i_vect.get_tuple() , 1)



		
	
