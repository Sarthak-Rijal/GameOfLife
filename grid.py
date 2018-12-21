
import pygame
from cell import cell
import sys
import array
pygame.init()

# cell class
class cell(object): 
    # Function to initialise the node object 

    def __init__(self, sizex, sizey, screen,cellSize = 40, buffer = 5):
        self.screen = screen
        self.sizex = sizex
        self.cellx = cellx
        self.celly = celly
        self.sizey = sizey
        self.cellSize = cellSize

        board = [[cell(screen, cellx, celly, False)]*sizex for i in range(sizey)]

    def _drawGrid(self):

        for i in range(self.sizex):
            for i in range(self.sizey):
                pygame.draw.rect(screen,BLACK,[ENEMY_POS_E[0],ENEMY_POS_E[1],SIZ_X,SIZ_Y])

