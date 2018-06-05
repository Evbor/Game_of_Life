#!/usr/bin/env python3

#
# model.py - program to get model of our project working
#            will use a class, to initialise grid, have a function
#            to invert the dead/alive value of a cell.
#			 and to evolve the grid values with time
#
# 29th May 2018 - Callum Jack
#
# Matplotlib functionality removed.
# 4th June 2018 - modified by Evan Borras
#

import numpy as np


################################################################################

class Model:


	def __init__(self, N=20,generations = 10):
		self.N = N
		self.generations = generations
		self.grid = np.zeros((N,N))
		self.initgrid = np.zeros((N,N))
		self.x_inv = []
		self.y_inv = []		
		for i in range(0,self.N):
			for j in range(0,self.N):
				if(np.random.randint(0,100)) < 10:
					self.initgrid[i][j] = 1
				else:
					pass

################################################################################

	def inv_point(self):    # function to find the array of inverted points for a grid setup
		self.x_inv = []
		self.y_inv = []
		
		for x in range(self.N):   # looping for each grid points
			for y in range(self.N):
				nalive = 0  # reset count each time
	
	

				nalive = (self.initgrid[(x-1)%self.N][y]+self.initgrid[(x+1)%self.N][y]+self.initgrid[x][(y+1)%self.N]+self.initgrid[x][(y-1)%self.N]+self.initgrid[(x-1)%self.N][(y-1)%self.N]+self.initgrid[(x-1)%self.N][(y+1)%self.N]+self.initgrid[(x+1)%self.N][(y-1)%self.N]+self.initgrid[(x+1)%self.N][(y+1)%self.N])

#counts neighbours



# when these conditions are true the point is to be inverted so append x and y into inversion arrays
				if (self.initgrid[x][y] ==1 and nalive <2):   # starvation
					self.x_inv = np.append(self.x_inv, x)
					self.y_inv = np.append(self.y_inv, y)

				if (self.initgrid[x][y] ==0 and nalive == 3): # reproduction
					self.x_inv = np.append(self.x_inv, x)
					self.y_inv = np.append(self.y_inv, y)

				if (self.initgrid[x][y] ==1 and nalive >3):    # overpopulation 
					self.x_inv = np.append(self.x_inv, x)
					self.y_inv = np.append(self.y_inv, y)   
		
				if(self.initgrid[x][y] == 1 and (nalive == 2 or nalive == 3)):  # continuity 
					continue
		 

################################################################################
	
	def invert(self, x, y):
		
		if (self.initgrid[x][y] == 1):   # function to swap values of grids (only feed invert arrays to this)
			self.grid[x][y] = 0
		else:
			self.grid[x][y] = 1
		


################################################################################


	def evolve(self):
	
		
		t = 1   #first generation
		self.inv_point()   # call initial inversion on gen -
		freq = 1          # how many evolutions between pictures
		
		
		while t <= self.generations:
				
			
			
			for i in range(len(self.x_inv)):  # inverting every point in the invert arrays
				x =int(self.x_inv[i])
				y =int(self.y_inv[i])
				self.invert(x,y)
	

			self.initgrid = self.grid.copy()   # making evolved grid become init

			t += 1          # go to next time step
			self.inv_point() # call inv to find grid points to be inverted in new generation
		
################################################################################


if __name__ == "__main__" :
	model = Model(N=20, generations = 10)
	model.evolve()		



