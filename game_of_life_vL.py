#!/usr/bin/env python3

################################################################################
#
# View and Controler for Game of Life App
#
#	This file defines our view object, and if run, creates instances of both our
#	model and view, activating both of them to run our Game of Life App.
#
#	3rd June 2018
#
################################################################################

#
# Importing Dependencies
#
#	tkinter - module for GUI design
#	module_inv - module that defines the model for our Game of Life App
#

import tkinter as tk
import model

#
# Defining our View Object
#

class View(object):

    # Initializing our View object: Model game ---> None
    def __init__(self, game):
        self.game = game
        self.root = self.create_root()
        self.pause = True
        self.menu_options = self.create_menu()
        self.cells = self.create_cells()
        self.root.after(0, self.animate)

    # Creates, initializes, and returns a root window with 2 resizeable grid
    # cells(row, column), (0,0), and (1,0).
    # None ---> Tk 
    def create_root(self):
        root = tk.Tk(className='game of life')
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        #for i in range(2):
            #root.grid_rowconfigure(i, weight=1)
        return root

    # Creates a Frame menu_frame inside cell (1,0) of root with two resizeable
    # grid cells (0,0) and (0,1). Creates a Button pause_button inside cell 
    # (0,0) of menu_frame, and a Button random_grid_btn inside cell (0,1) of 
    # menu_frame.
    # None ---> Button
    def create_menu(self):
        menu_options = {}
        menu_frame = tk.Frame(self.root)
        menu_frame.grid(row=1, column=0, sticky="NSEW")
        menu_frame.grid_rowconfigure(0, weight=1)
        #making pause button
        menu_frame.grid_columnconfigure(0, weight=1)
        pause_button = tk.Button(menu_frame, text="Start", command=self.stop_start)
        pause_button.grid(row=0, column=0, sticky="NSEW")
        menu_options['Pause Button'] = pause_button
        #making random button
        menu_frame.grid_columnconfigure(1, weight=1)
        random_grid_btn = tk.Button(menu_frame, text="Random", command=self.randomize)
        random_grid_btn.grid(row=0, column=1, sticky="NSEW")
        menu_options['Random Button'] = random_grid_btn
        ########################################################################
        #
        # Add code to make your buttons that belong in the menu bar here.
        #
        # Your first line should be menu_frame.grid_columnconfigure(2, weight=1)
        # this configures the second column of menu_frames grid to be shrinkable
        # You should then generate your widget add it to menu_frame's cell 
        # (row=0, column=2). Make sure at the end of generating and configuring
        # your widget to add it to the dictionary menu_options, which is an
        # attribute of our View class. Any code that is run when a user
        # interacts with your widget should be contained in another function 
        # that you make outside of this function.
        #
        ########################################################################
        return menu_options

    # Creates a Frame cell_frame inside cell (0,0) of root with a resizeable
    # grid cell (row,column) corresponding to each (row,column) value in the 
    # NxN array game.grid. Creates a Button btn for each grid cell in cell_frame
    # where each cell is yellow if game.grid[row][column] = 1 (cell is alive)
    # blue otherwise (cell is dead). 
    # None ---> Button [row][column]
    def create_cells(self):
        cell_frame = tk.Frame(self.root)
        cell_frame.grid(row=0, column=0, sticky="NSEW")
        cells = []
        for r in range(len(self.game.grid)):
            cell_frame.grid_rowconfigure(r, weight=1)
            cells_r = []
            for c in range(len(self.game.grid[r])):
                cell_frame.grid_columnconfigure(c, weight=1)
                color = "blue"
                if (self.game.grid[r][c] == 1):
                    color = "yellow"
                btn = tk.Button(cell_frame, bg=color, command=lambda r=r,c=c: self.set_cell(r,c))
                btn.grid(row=r, column=c, sticky="NSEW")
                cells_r.append(btn)
            cells.append(cells_r)
        return cells

    # Sets the color of Button cells[row][col] to yellow if
    # abs(game.grid[row][col] - 1) = 1 (cell is alive) and blue otherwise
    # (cell is dead). Sets game.grid[row][col] to the value computed that
    # determines the button's color. This method is called on a click Event of
    # Button cells[row][col].
    # int row, int col ---> None
    def set_cell(self, row, col):
        self.game.grid[row][col] = abs(self.game.grid[row][col] - 1)
        if (self.game.grid[row][col] == 1):
            self.cells[row][col]['bg'] = "yellow"
        else:
            self.cells[row][col]['bg'] = "blue"

    # Stops and starts the animation. If pause is set to not pause, and if pause
    # is True then the text of the pause_button is set to Start. If pause is
    # False then the text of pause_button is set to Pause and animate() is
    # called. This method is called on a click Event of Button pause_button.
    # None ---> None
    def stop_start(self):
        self.pause = not self.pause
        if not self.pause:
            self.menu_options['Pause Button']['text'] = "Pause"
            self.animate()
        else:
            self.menu_options['Pause Button']['text'] = "Start"

    def randomize(self):
        game.rand()
        self.update_cells()        

    # Updates the color of each Button cells[r][c] to yellow if
    # game.grid[r][c] = 1 (cell is alive) and to blue otherwise.
    # None ---> None
    def update_cells(self):
        for r in range(len(self.game.grid)):
            for c in range(len(self.game.grid[r])):
                if (self.game.grid[r][c] == 1):
                    self.cells[r][c]['bg'] = "yellow"
                else:
                    self.cells[r][c]['bg'] = "blue"

    # Animates the our grid of buttons if pause is set to False. If pause is
    # False then game is evolved by calling game.evolve() and cells is
    # updated to reflect this evolution by calling update_cells(). animate()
    # is then called after 15 frames passes.
    # None ---> None
    def animate(self):
        if not self.pause:
            self.game.evolve()
            self.update_cells()
            self.root.after(200, self.animate)

    # Starts the mainloop of the root window by calling root.mainloop().
    # None ---> None
    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    game = model.Model(20)
    view = View(game)
    view.start()

