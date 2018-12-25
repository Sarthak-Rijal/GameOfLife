from cell import cell
import pygame
import sys
import random
import array
import math

pygame.init()

#arbritary screen size and setup 
size = (2255, 1360)
screen = pygame.display.set_mode(size)
grid_color = (192,192,192)

#FPS
clock = pygame.time.Clock()
FPS = 60


ROW = 30#rows
COL = 50#columns

#GLOBAL CELL ATTRIBUTES
margin = 5
CELL_SIZE = 40

pressed = False



# MAKE THE GRID
#Generates the Grid where the simulation occurs
GRID = []
for i in range(COL):
    column = []
    for j in range(ROW):
        column.append(cell(screen, False, i, j, margin + (CELL_SIZE + margin)*i, 
                                                margin + (CELL_SIZE + margin)*j, 
                                                color = grid_color ))
    GRID.append(column)


#
#is there a better way better way?
#connects each cell in the grid with its neighbours
for i in range(COL):
    for j in range(ROW):
        #connected the corners
        #top left
        if (i == 0 and j == 0):            

            GRID[i][j].addNeigbour([GRID[i+1][j], GRID[i+1][j+1], GRID[i][j+1]])
            
        #bottom left
        elif (i == 0 and j == ROW - 1):

            GRID[i][j].addNeigbour([GRID[i+1][j], GRID[i+1][j-1], GRID[i][j-1]])
            
        #bottom right
        elif (i == COL - 1 and j == ROW - 1):

            GRID[i][j].addNeigbour([GRID[i-1][j], GRID[i-1][j-1], GRID[i][j-1]])
        #top right
        elif (i == COL - 1 and j == 0 ):

            GRID[i][j].addNeigbour([GRID[i-1][j], GRID[i-1][j+1], GRID[i][j-1]])


        #connecting the edges - the corners
        #left edge not including topLeft and bottomLeft corners
        elif (i == 0 and not ((i == 0 and j == 0) or (i == 0 and j == ROW - 1))):

            GRID[i][j].addNeigbour([GRID[i][j-1], GRID[i+1][j-1], GRID[i+1][j], GRID[i+1][j+1]])

        #right edge not including topRight and Bottom right
        elif (i == COL - 1 and not ((i == COL - 1 and j == 0) or (i == COL - 1 and j == ROW - 1))):

            GRID[i][j].addNeigbour([GRID[i][j-1], GRID[i-1][j-1], GRID[i-1][j], GRID[i-1][j+1], GRID[i][j+1]])
        #top edge not including topLeft and topRight
        elif (j == 0 and not ((i == 0 and j == 0) or (i == COL - 1 and j == 0))):

            GRID[i][j].addNeigbour([GRID[i+1][j], GRID[i+1][j+1], GRID[i][j+1], GRID[i-1][j+1], GRID[i-1][j]])
        #bottom edge
        elif (j == ROW - 1 and not ((i == 0 and j == ROW - 1) or (i == COL - 1 and j == ROW - 1))):

            GRID[i][j].addNeigbour([GRID[i+1][j], GRID[i+1][j-1], GRID[i][j-1], GRID[i-1][j-1], GRID[i-1][j]])

        #every thing else 
        else:
            GRID[i][j].addNeigbour([ GRID[i+1][j], GRID[i+1][j-1], GRID[i][j-1], GRID[i-1][j-1], 
                                     GRID[i-1][j], GRID[i+1][j+1], GRID[i][j+1], GRID[i-1][j+1] ])

#initially draws grid with all thecells
for i in range(COL):
            for j in range(ROW):
                GRID[i][j]._draw(screen)
                
def play(GRID, pressed):

    toLive = []
    toDie = []

    while True:

       #gets the mouse position
        x,y = pygame.mouse.get_pos()

        #event listner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #toggles full screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                if screen.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode(size)
                else:
                    pygame.display.set_mode(size, pygame.FULLSCREEN)

            #resets the drawing board
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                for i in range(COL):
                    for j in range(ROW):
                        GRID[i][j].dead()
            
            #toggles between simulation and drawing 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pressed = not pressed

        #runs the simulation
        if pressed:
            for i in range(COL):
                for j in range(ROW):
                    GRID[i][j]._draw(screen)

                    #reads the grid and stores the cells that need to die and stores it in die
                    die = GRID[i][j].update_toDie()
                    if (die != [] and die not in toDie):
                        toDie.append(die)

                    #reads the grid and stores the cells that need to live or come alive and stores it in live
                    live = GRID[i][j].update_toLive()
                    if (live != [] and live not in toLive):
                        toLive.append(live)
                    
            #updates the cells that need to die or live 
            #and clear the storage
            
            for i in toDie:
                GRID[i[0]][i[1]].dead()
            for i in toLive:
                GRID[i[0]][i[1]].pressedAlive()
            toDie.clear()
            toLive.clear()

            #delays the 
            pygame.time.wait(100)

        #drawing part 
        else:
            for i in range(COL):
                for j in range(ROW):
                    GRID[i][j]._draw(screen)
                    GRID[i][j].detect_mouse(x, y)

        pygame.display.update()
        clock.tick(FPS)

play(GRID, pressed)