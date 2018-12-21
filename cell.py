import pygame
import sys
pygame.init()

# cell class
class cell(object): 
    # Function to initialise the node object 
    def __init__(self, screen, DOA, x, y, coor_x, coor_y, size = 40, color = (0,0,0), margin = 5):
        self.margin = margin
        self.x = x
        self.y = y
        self.coor_x = coor_x
        self.coor_y = coor_y
        self.screen = screen
        self.color = color
        self.size = size 
        self.rect = pygame.Rect(self.coor_x, self.coor_y, self.size, self.size)
        self.DOA = DOA  # Assign data 
        self.N = None
        self.E = None
        self.S = None
        self.W = None
        self.NE = None
        self.SE = None
        self.NW = None
        self.SW = None

        if (self.DOA):
            self.color = (0,0,0)

    def detect_mouse(self, x, y, left, right):
        if (self.rect.collidepoint(x,y)):
            self.color = (0,0,0)
        else:
            self.color = (192, 192, 192)

    def changeDOA(self):
        self.DOA = not self.DOA


            

        
    
    def _draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
                                                  



   # def countNeighbout(self): nee to count neighbours
       
        