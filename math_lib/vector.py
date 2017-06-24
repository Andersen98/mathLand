import logging, sys

class Vector(object):
	def __init__(self, i, j, k = None):
		"""Initialize the vector class. Vector Dim is given based on user input"""
		self.i = float(0)
		self.j = float(0)
		self.k = float(0)
		self.dim = 0
		logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
		
		if(k is None):
			self.dim = 2
			self.set_vec(i, j)

		else:
			self.dim = 3
			self.set_vec(i, j, k)


	def set_vec(self, i, j, k = None):
		"""Sets the components when given 2 or 3 input params. Give 3 params for 3d and 2 params for 2d"""
		if (k is None) and (self.dim == 3):
			logging.error("Expecting a 3d vector but you only gave me two components")
		elif (not (k is None)) and (self.dim == 2):
			logging.error("Expecting a 3d vector but you only gave me two components")
		elif self.dim == 2:
			self.i = i
			self.j = j
		else:
			self.i = i
			self.j = j
			self.k = k

	def add(self, vector_b):
		"""Adds a given vector to another and returns the sum as a third vector object"""
		i = vector_b.get_i() + self.i
		j = vector_b.get_j() + self.j
		result = None
		if vector_b.get_dim == 3:
			result = Vector(i,j,vector_b.get_k + self.k)
		else:
			result = Vector(i,j)
		return result
	def mult_scalar(self, a):
		"""Multiplies vector by scalar and returns result"""
		i = self.i * a
		j = self.j * a
		k = 0
		result = None
		if self.dim ==3:
			k = self.k * a
			result = Vector(i,j,k)
		else:
			result = Vector(i,j)
		return result
		

	def get_dim(self):
		return self.dim
	def get_i(self):
		return self.i
	def get_j(self):
		return self.j
	def get_k(self):
		result = 0
		if self.dim == 2:
			logging.error("Cannot return a 3rd component for a 2d vector")
		else:
			result = self.k		
		return result

	def get_tuple(self):
		return(self.i,self.j)

	def print_vect(self):
		"""Prints the vector components to the screen"""
		if self.dim == 3:
			print(str(self.i) + ", " + str(self.j) + ", " + str(self.k) )
		else:
			print(str(self.i) + " " + str(self.j))

