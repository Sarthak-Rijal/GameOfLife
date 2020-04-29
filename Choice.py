import pygame
import sys
import random

pygame.init()

BLACK = (0,0,0)
GREY = (192, 192, 192)
# cell class
class Choice(object): 
    # Function to initialise the node object 
    def __init__(self, x, y, width, height, msg, cellSize,  fileNum):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.msg = msg
        self.cellSize = cellSize
        self.fileNum = fileNum

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.pressed = False
        self.color = (255,0,0)


    #detects the mouse hovering, logic of clicking a cell
    def detect_mouse(self, x, y):
        if (self.rect.collidepoint(x,y)):
            self.color = (192,192,192)
            if (pygame.mouse.get_pressed()[0]):
                return fileNum
        



    def print_f(self,screen,msg,color):#,x,y):
        Text = pygame.font.Font("freesansbold.ttf", 50)
        write = Text.render(msg,True,color)
        write_rect = write.get_rect()
        write_rect.center = ((self.x+self.x/11),(self.y + self.y/12))
        screen.blit(write,write_rect)

    def update(self, screen):

        rect = [self.x, self.y, self.width, self.height]

        pygame.draw.rect(screen, (252 + .025, 247, 18), rect)

        self.print_f(screen, self.msg, (0,0,0))


        
        

    
        