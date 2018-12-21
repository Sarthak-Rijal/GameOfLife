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
size = (2255, 1405)
screen = pygame.display.set_mode(size)
grid_color = (192,192,192)
#FPS
clock = pygame.time.Clock()
FPS = 60

row = 30#rows
col = 50#columns

#GLOBAL CELL ATTRIBUTES
margin = 5
CELL_SIZE = 40

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
    

for j in range(row):
    for i in range(col):
            GRID[i][j]._draw(screen)


while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                if screen.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode(size)
                else:
                    pygame.display.set_mode(size, pygame.FULLSCREEN)
        
        for j in range(row):
            for i in range(col):
                GRID[i][j]._draw(screen)

        x,y = pygame.mouse.get_pos()
        left_mouse, idk, right_mouse = pygame.mouse.get_pressed() #b1 is left click, b2 is right click
        
        #check for mouse hover
        for j in range(row):
            for i in range(col):
                GRID[i][j].detect_mouse(x,y, left_mouse, right_mouse)
                #GRID[i][j].pressed_mouse(x, y, b1, b3)

                

    # pygame.draw.rect(screen, (255,255,255),[40+margin+margin, 0+margin+margin, 40,40] )


        pygame.display.update()
        clock.tick(FPS)

			