import pygame
from vector import Vector

class Environment(object):
	"""Environment class holds the state of the environment"""
	def __init__(self):
		"""Initialized to have (1,0) (0,1) coordinate system"""
		self.vect_i = Vector(1,0)
		self.vect_j = Vector(0,1)
		self.origin = Vector(0,0)
		#Scales are in pixels
		self.scale = 100
	def set_origin(self,origin):
		"""Sets the origin"""
		self.origin = origin

	def get_origin(self):
		"""returns origin"""
		return self.origin

	def get_i_vect(self):
		"""Gets the scaled version of the i unit vector"""
		result = self.vect_i.mult_scalar(self.scale)
		return result

	def get_j_vect(self):
		"""Gets the scaled version of the j unit vector"""
		result = self.vect_j.mult_scalar(self.scale)
		return result

