from cell import cell
from btn import *
import pygame
import sys
import random
import array
import math
import pickle

pygame.init()


#arbritary screen size and setup 
size = (2700, 1600)
screen = pygame.display.set_mode(size)
grid_color = (255,255,255)

#GLOBAL CELL ATTRIBUTES
margin = 1


#FPS
clock = pygame.time.Clock()
FPS = 60





pressed = False


def readData(GRID, GRID_DATA, COL, ROW, CELL_SIZE):
    for i in range(COL):
        column = []
        for j in range(ROW):
            column.append(cell(screen, GRID_DATA[i][j][0], i, j,
                                                    margin + (CELL_SIZE + margin)*i, 
                                                    margin + (CELL_SIZE + margin)*j, 
                                                    grid_color, CELL_SIZE ))
        GRID.append(column)


                
def play(pressed, f):

#comment out when doing #Load Grid
##############################################################################################
    CELL_SIZE = 40
    ROW = (size[1])/CELL_SIZE #rows #original 30
    COL = ((size[0] - (size[0]/10)) /CELL_SIZE) #creates the space in the side

#LOAD GRID
###################################################################################################
    # MAKE THE GRID
    GRID = []
    #Generates the Grid where the simulation occurs
    
    
    with open(f, 'rb') as file:
        GRID_DATA = pickle.load(file)
    
    CELL_SIZE = GRID_DATA[-1]
    ROW = (size[1])/CELL_SIZE #rows #original 30
    COL = ((size[0] - (size[0]/10)) /CELL_SIZE)    
    readData(GRID, GRID_DATA, COL, ROW, CELL_SIZE)

    
    for i in range(COL):
        for j in range(ROW):
            if (GRID_DATA[i][j][0]):
                GRID[i][j].pressedAlive()
    
    
    
#MAKE GRID 
####################################################################################
    """
    GRID_DATA = []
    for i in range(COL):
        data = []
        for j in range(ROW):
            data.append([False])

        GRID_DATA.append(data)
    GRID_DATA.append(CELL_SIZE)

    readData(GRID, GRID_DATA, COL, ROW, CELL_SIZE)
    """

    

###################################################################################SS

    

    
    file = ["0)Empty", "1)Pulsar", "2)Glider", "3)Glider-Gun", "4)Hammerhead", "5)LinePuffer", "6)Box", "7)Smile", "8)Fish Face", "9)Tony"]


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



#####################################
    
    Buttons = []
    for i in range(10):
        Buttons.append(btn((size[0] - (size[0]/10)), (i*160)+1, (size[0]/10), 160, file[i], 80, i))


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
                play(pressed, f)

            
            #toggles between simulation and drawing ss
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pressed = not pressed

            #pickles the current data
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                with open('pulsarStarter.pkl', 'wb') as file:
                    pickle.dump(GRID_DATA, file)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                screen.fill((0,0,0))
                play(False, "Empty.pkl")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                screen.fill((0,0,0))
                play(False, "Pulsar.pkl")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                screen.fill((0,0,0))
                play(False, "Glider.pkl")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                screen.fill((0,0,0))
                play(False, "Glider_Gun.pkl")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                screen.fill((0,0,0))
                play(False, "Hammerhead.pkl")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                screen.fill((0,0,0))
                play(False, "LinePuffer.pkl")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
                screen.fill((0,0,0))
                play(False, "Box.pkl")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_7:
                screen.fill((0,0,0))
                play(False, "Smile.pkl")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_8:
                screen.fill((0,0,0))
                play(False, "fishFace.pkl")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_9:
                screen.fill((0,0,0))
                play(False, "pulsarStarter.pkl")



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
            del toDie[:]
            del toLive[:]

            #delays the 
            pygame.time.wait(100)

        #drawing part # updating data
        else:
            for i in range(COL):
                for j in range(ROW):
                    GRID[i][j]._draw(screen)
                    GRID[i][j].detect_mouse(x, y)

                    GRID_DATA[i][j][0] = GRID[i][j].DOA


        for i in Buttons:
            i.update(screen)
        
        pygame.display.update()
        clock.tick(FPS)


play(pressed, "Empty.pkl")