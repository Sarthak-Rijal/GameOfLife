import pygame
import sys
import random
pygame.init()

# cell class
class cell(object): 
    # Function to initialise the node object 
    def __init__(self, screen, DOA, x, y, coor_x, coor_y, color, size, pressed = False,
                                                   neighbours = []):
        self.x = x
        self.y = y
        self.coor_x = coor_x
        self.coor_y = coor_y
        self.screen = screen
        self.color = color
        self.size = size 
        self.rect = pygame.Rect(self.coor_x, self.coor_y, self.size, self.size)
        self.DOA = DOA  # Assign data 
        self.pressed = pressed
        self.neighbours = neighbours

    #detects the mouse hovering, logic of clicking a cell
    def detect_mouse(self, x, y):
        if (self.rect.collidepoint(x,y)):
            self.potentiallyAlive()
            if (pygame.mouse.get_pressed()[0]):
                self.pressedAlive()
            elif (pygame.mouse.get_pressed()[2]):
                self.dead()
        else:
            if(not self.pressed):
                self.dead()

    #makes the cell dead 
    def dead(self):
        self.pressed = False
        self.DOA = False
        self.color = (255,255,255)

    #makes the cell alive
    def potentiallyAlive(self):
        self.color = (random.randrange(0,255), random.randrange(0,255),random.randrange(0,255))


    #makes the cell alive when clicked
    def pressedAlive(self):
        self.pressed = True
        self.DOA = True
        self.color = (random.randrange(0,255), random.randrange(0,255),random.randrange(0,255))

    
    def addNeigbour(self, neighbour):
        self.neighbours = neighbour
        
    #draws the cell
    def _draw (self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
                                                  

    def countAliveNeighbour (self):
        neighbours_alive = 0
        for i in self.neighbours:
            if (i.DOA == True):
                neighbours_alive += 1
        return neighbours_alive

    def toString(self):
        return str(self.x)+","+str(self.y)

    def update_toDie(self):
        alive_near = self.countAliveNeighbour()
        if (self.DOA == True):           
            if (alive_near == 0 or alive_near == 1):
                return [self.x,self.y]
            if (alive_near > 3):
                return [self.x,self.y]
            else:
                return []
        else:
            return []

    def update_toLive(self):
        alive_near = self.countAliveNeighbour()
        if (self.DOA == False):
            if (alive_near == 3):
                return [self.x,self.y]
            else:
                return []
        else:
            return []
        if (self.DOA == True):
            if (alive_near == 2 or alive_near == 3):
                return [self.x,self.y]
            else:
                return []
        else:
            return[]

            



    #rules of the game

    # 1) Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    # 2) Any live cell with two or three live neighbors lives on to the next generation.
    # 3) Any live cell with more than three live neighbors dies, as if by overpopulation.
    # 4) Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

   #def countNeighbout(self): need to count neighbours
       
        