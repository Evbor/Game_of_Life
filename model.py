#!/usr/bin/env python3

#
# model.py - program to get model of our project working
#            will use a class, to initialise grid, have a function
#            to invert the dead/alive value of a cell.
#			 and to evolve the grid values with time
#
# 29th May 2018 - Callum Jack
#

import numpy as np


################################################################################

class Model:


	def __init__(self, N=50):
		self.N = N
		self.grid = np.zeros((N,N))
		self.initgrid = np.zeros((N,N))
		self.x_inv = []
		self.y_inv = []		
	

################################################################################

	def rand(self):
		for i in range(0,self.N):
				for j in range(0,self.N):
					if int(100*np.random.random()) < 15:  # initalse random grid 
						self.grid[i][j] = 1
					else:
						self.grid[i][j] = 0

################################################################################

	def inv_point(self):    # function to find the array of inverted points for a grid setup
		self.x_inv = []
		self.y_inv = []
		
		for x in range(self.N):   # looping for each grid points
			for y in range(self.N):
				nalive = 0  # reset count each time
	
				if (x == (self.N -1) and y != (self.N -1)):
					nalive = (
self.initgrid[(x-1)][y]
+self.initgrid[0][y]
+self.initgrid[x][(y+1)]
+self.initgrid[x][(y-1)]
+self.initgrid[(x-1)][(y-1)]
+self.initgrid[(x-1)][(y+1)]
+self.initgrid[0][(y-1)]
+self.initgrid[0][(y+1)])
	
				elif (y == (self.N -1) and x != (self.N -1)):
					nalive = (self.initgrid[(x-1)][y]
+self.initgrid[(x+1)][y]
+self.initgrid[x][0]
+self.initgrid[x][(y-1)]
+self.initgrid[(x-1)][(y-1)]
+self.initgrid[(x-1)][0]
+self.initgrid[(x+1)][(y-1)]
+self.initgrid[(x+1)][0])

				elif y == (self.N -1) and x == (self.N -1):
					nalive = (self.initgrid[(x-1)][y]
+self.initgrid[(0)][y]
+self.initgrid[x][0]
+self.initgrid[x][(y-1)]
+self.initgrid[(x-1)][(y-1)]
+self.initgrid[(x-1)][0]
+self.initgrid[0][(y-1)]
+self.initgrid[0][0])

				else:

					nalive = (self.initgrid[(x-1)][y]
+self.initgrid[(x+1)][y]
+self.initgrid[x][(y+1)]
+self.initgrid[x][(y-1)]
+self.initgrid[(x-1)][(y-1)]
+self.initgrid[(x-1)][(y+1)]
+self.initgrid[(x+1)][(y-1)]
+self.initgrid[(x+1)][(y+1)])




# when these conditions are true the point is to be inverted so append x and y into inversion arrays
				if (self.initgrid[x][y] ==1 and ((nalive < 2) or (nalive > 3))):  
														 # starvation + overpop
					self.x_inv = np.append(self.x_inv, x)
					self.y_inv = np.append(self.y_inv, y)

				if (self.initgrid[x][y] ==0 and nalive == 3): # reproduction
					self.x_inv = np.append(self.x_inv, x)
					self.y_inv = np.append(self.y_inv, y)
					

################################################################################
	
	def invert(self, x, y):
		
		if (self.initgrid[x][y] == 1):   # function to swap values of grids (only feed invert arrays to this)
			self.grid[x][y] = 0
		else:
			self.grid[x][y] = 1
		


################################################################################


	def evolve(self):						
		
		self.inv_point()   # call initial inversion
		 											
			
		for i in range(len(self.x_inv)):  # inverting every point in the invert arrays
			x =int(self.x_inv[i])
			y =int(self.y_inv[i])
			self.invert(x,y)
		
			
		self.initgrid = self.grid.copy()   # making evolved grid become init

		         
		self.inv_point() # call inv to find grid points to be inverted in new generation
		
################################################################################


if __name__ == "__main__" :
	model = Model()
	model.evolve()		



