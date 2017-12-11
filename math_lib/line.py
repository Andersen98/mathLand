import logging, sys
import pygame
from environment import Environment
from vector import Vector

class Line(object):
	"""Linear Combination of line is represented as linear comb of basis vectors"""
	#mathematically all lines can be represented as a linear comb. of the basis vectors from the env and offset from origin
	def __init__(self, evnvironment a, b, c = None):
		#Linear comb of basis vectors, a -> i, b -> j, c -> k
        self.a = a
		self.b = b
		self.dim = 2
		if c is None:
			self.dim = 3
			self.c = c
		self.environment = environment
		
	def update(self,environment):
		self.environment = environment
	
	def draw(self,screen):