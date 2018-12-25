#!/usr/bin/python
# -*- coding: utf-8 -*-
from cell import cell
import pygame
import sys
import random
import array
import math

pygame.init()

#screen size and setup
size = (2255, 1360)
screen = pygame.display.set_mode(size)
grid_color = (192,192,192)
#FPS
clock = pygame.time.Clock()
FPS = 200

row = 30#rows
col = 50#columns

#GLOBAL CELL ATTRIBUTES
margin = 5
CELL_SIZE = 40

pressed = False


# MAKE THE GRID
#hardcoded number of grids and 
GRID = []
for i in range(col):
    column = []
    for j in range(row):
        column.append(cell(screen, False, i, j, margin + (CELL_SIZE + margin)*i, 
                                                margin + (CELL_SIZE + margin)*j, 
                                                color = grid_color ))
    GRID.append(column)



#can i do this in a better way?
for i in range(col):
    for j in range(row):
        #connected the corners
        #top left
        if (i == 0 and j == 0):            
            GRID[i][j].addNeigbour([GRID[i+1][j], GRID[i+1][j+1], GRID[i][j+1]])
            
        #bottom left
        elif (i == 0 and j == row - 1):
            GRID[i][j].addNeigbour([GRID[i+1][j], GRID[i+1][j-1], GRID[i][j-1]])
            
        #bottom right
        elif (i == col - 1 and j == row - 1):
            GRID[i][j].addNeigbour([GRID[i-1][j], GRID[i-1][j-1], GRID[i][j-1]])
        #top right
        elif (i == col - 1 and j == 0 ):
            GRID[i][j].addNeigbour([GRID[i-1][j], GRID[i-1][j+1], GRID[i][j-1]])


        #connecting the edges - the corners
        #left edge not including topLeft and bottomLeft corners
        elif (i == 0 and not ((i == 0 and j == 0) or (i == 0 and j == row - 1))):
            GRID[i][j].addNeigbour([GRID[i][j-1], GRID[i+1][j-1], GRID[i+1][j], GRID[i+1][j+1]])#, GRID[i][j+1]])
        #right edge not including topRight and Bottom right
        elif (i == col - 1 and not ((i == col - 1 and j == 0) or (i == col - 1 and j == row - 1))):
            GRID[i][j].addNeigbour([GRID[i][j-1], GRID[i-1][j-1], GRID[i-1][j], GRID[i-1][j+1], GRID[i][j+1]])
        #top edge not including topLeft and topRight
        elif (j == 0 and not ((i == 0 and j == 0) or (i == col - 1 and j == 0))):
            GRID[i][j].addNeigbour([GRID[i+1][j], GRID[i+1][j+1], GRID[i][j+1], GRID[i-1][j+1], GRID[i-1][j]])
        #bottom edge
        elif (j == row - 1 and not ((i == 0 and j == row - 1) or (i == col - 1 and j == row - 1))):
            GRID[i][j].addNeigbour([GRID[i+1][j], GRID[i+1][j-1], GRID[i][j-1], GRID[i-1][j-1], GRID[i-1][j]])

        #every thing else 
        else:
            GRID[i][j].addNeigbour([ GRID[i+1][j], GRID[i+1][j-1], GRID[i][j-1], GRID[i-1][j-1], 
                                     GRID[i-1][j], GRID[i+1][j+1], GRID[i][j+1], GRID[i-1][j+1] ])


for i in range(col):
            for j in range(row):
                GRID[i][j]._draw(screen)
                


def print_f(msg,siz,color,x,y):
    Text = pygame.font.Font("bit5x3.ttf",siz)
    write = Text.render(msg,True,color)
    write_rect = write.get_rect()
    write_rect.center = ((x),(y))
    screen.blit(write,write_rect)

    

def play(GRID, pressed):
    while True:
        
        x,y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                if screen.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode(size)
                else:
                    pygame.display.set_mode(size, pygame.FULLSCREEN)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                GRID = []
                for i in range(col):
                    column = []
                    for j in range(row):
                        column.append(cell(screen, False, i, j, margin + (CELL_SIZE + margin)*i, 
                                                                margin + (CELL_SIZE + margin)*j, 
                                                                color = grid_color ))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pressed = not pressed

        # for i in range(col):
        #     for j in range(row):
        #         GRID[i][j]._draw(screen)
        #         GRID[i][j].detect_mouse(x,y) 
        #         l = str(GRID[i][j].x)
        #         k = str(GRID[i][j].y)
        #         print_f(l+","+k, 20, (0,0,0), GRID[i][j].coor_x+20,  GRID[i][j].coor_y+20)

        if pressed:
            for j in range(row):
                for i in range(col):
                    GRID[i][j]._draw(screen)
                    GRID[i][j].update()
        else:
            for j in range(row):
                for i in range(col):
                    GRID[i][j]._draw(screen)
                    GRID[i][j].detect_mouse(x, y)
        
       #DEBUGGING COORDINATES
        coorx = 20
        coory = 20
        
        print_f("THIS", 20, (0,0,0), GRID[coorx][coory].coor_x+20,  GRID[coorx][coory].coor_y+20)
        print(GRID[coorx][coory].countAliveNeighbour())

        pygame.display.update()
        clock.tick(FPS)

play(GRID, pressed)