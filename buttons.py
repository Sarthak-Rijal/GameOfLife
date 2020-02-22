import pygame
import sys
pygame.init()

width = 800
height = 500

screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("BUTTONS")

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,255,0)
X=0

def print_f(msg,siz,color,x,y):
    Text = pygame.font.Font("freesansbold.ttf",siz)
    write = Text.render(msg,True,color)
    write_rect = write.get_rect()
    write_rect.center = ((x),(y))
    screen.blit(write,write_rect)

def mouse_point(btn_x,btn_y,W,H, mouse):
    if btn_x + W > mouse[0] > btn_x and btn_y + H > mouse[1] > btn_y:
        return True
        
def button(color,x,y,w,h,msg):
    pygame.draw.rect(screen,color,[x,y,w,h])
    print_f(msg,w,BLACK,x+(w/2),y+(h/2))

    
    
def button_press(D_color,color,x,y,w,h,msg,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button(color,x,y,w,h,msg)

    if mouse_point(x,y,w,h,mouse):
        color_change = button(D_color,x,y,w,h,msg)
        if mouse[0] == 1 and action == "5":
            global storage
            storage.append(action)

def num_sto(sto,store,number):
    if len(store) == 4:
        sto.append(store[0]),sto.append(store[1]), sto.append(store[2])
        del store[:]
    store.append(number)

def display_number(store):
    if len(store)==1:
        print_f(str(store[0]),40,BLACK,100,100)
    if len(store)==2:
        print_f(str(store[0]),40,BLACK,100,100)
        print_f(str(store[1]),40,BLACK,200,100)
    if len(store)==3:
        print_f(str(store[0]),40,BLACK,100,100)
        print_f(str(store[1]),40,BLACK,200,100)
        print_f(str(store[2]),40,BLACK,300,100)

def display_used(sto,used):
    for i in range(used):
        if used == 3 or 6 or 9 or 12 or 15 or 18 or 21 or 24 or 27 or 30:
            if i == 0:
                print_f(str(sto[0]),16,BLACK,100,300)
            else:
                print_f(str(sto[((i*3)-3)]),16,BLACK,100,300)
            if i == 0:
                print_f(str(sto[1]),16,BLACK,200,300)
            else:
                print_f(str(sto[((i*3)-2)]),16,BLACK,200,300)
            if i == 0:
                print_f(str(sto[2]),16,BLACK,300,300)
            else:
                print_f(str(sto[((i*3)-1)]),16,BLACK,300,300)
            
        
def game_loop():
    store = []
    sto = []
    x,y,z = 0,1,2
    w = 0
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if mouse_point(400,250,50,50,mouse):
                    num_sto(sto,store,5)
                if len(store)==4:
                    w+=3
                
                    
                    

        screen.fill(WHITE)
        button_press(BLACK,BLUE,400,250,50,50,"HELLO",action="5")
        print store
        display_number(store)
        display_used(sto,(len(sto)/3))
        
        pygame.display.update()
game_loop()
