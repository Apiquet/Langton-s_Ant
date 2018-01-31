import pygame
from pygame.locals import *

import time

Nbr_Cell_x = 70
Nbr_Cell_y = 70

Cell_Size= 8

#Color cell = Blue
Cell_ON = (68,101,182)
Cell_OFF = (255,255,255)

WITDH = Nbr_Cell_x * Cell_Size
HEIGHT = Nbr_Cell_y * Cell_Size

def main():
    #pygame initialized
    pygame.init()
    pygame.display.set_caption("Laugton s Ant")
    #creation of the window
    window = pygame.display.set_mode((WITDH,HEIGHT))
    #creation of the board
    board= initialize_board()
    pause = True
    posx=Nbr_Cell_x/2
    posy=Nbr_Cell_y/2
    dir_ant = "haut"

    #number of the generation
    generation = 0 
    #speed of the game
    speed = 0  
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            #pause game with space key
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pause = not pause
                if event.key == K_r:                
                    window.fill(Cell_dead)                    
                    board=initialize_board()                 
                if event.key == K_UP:
                    speed+=1 
            
        #update the board state to the next generation
        if not pause:
            time.sleep(1)
            board, posx, posy = update_board(board, dir_ant, posx, posy)
            generation += 1
            #display generation number
            print("Generation {}".format(generation))
            #fill the window with only dead cells
            window.fill(Cell_OFF)        
               
        #draw on the window each cell alive
        for y in range(Nbr_Cell_y):
            for x in range(Nbr_Cell_x):
                if board[y][x]:
                    pygame.draw.rect(window, Cell_ON, (x * Cell_Size, y * Cell_Size, Cell_Size, Cell_Size))
        #display the result
        pygame.display.update()           
    
def initialize_board():
    return [[False for x in range(Nbr_Cell_x)] for y in range(Nbr_Cell_y)]

def update_board(board, dir_ant, x, y):
    next_board= initialize_board()
    next_x=0
    next_y=0 
    for x in range(Nbr_Cell_y):
        for y in range(Nbr_Cell_x):
            next_x, next_y, dir_aut = find_ant_turn(board, dir_ant, x, y)
            if board[y][x]:
                next_board[y][x] = False
            else:
                next_board[y][x] = True
    return next_board, next_x, next_y

def find_ant_turn(board, dir_ant, x, y):
    next_dir=""
    next_x=0
    next_y=0
    if board[y][x] == True:
        next_x, next_y, next_dir = find_right_cell(board, dir_ant, x, y)
    if board[y][x] == False:
        next_x, next_y, next_dir = find_left_cell(board, dir_ant, x, y)
    return x, y, next_dir

def find_right_cell(board, dir_ant, x, y):
    if dir_ant == "haut":
        return (x+1), y, "droite"
    if dir_ant == "bas":
        return (x-1), y, "gauche"
    if dir_ant == "gauche":
        return x, y+1, "haut"
    if dir_ant == "droite":
        return x, y-1, "bas"

def find_left_cell(board, dir_ant, x, y):
    if dir_ant == "haut":
        return (x-1), y, "gauche"
    if dir_ant == "bas":
        return (x+1), y, "droite"
    if dir_ant == "gauche":
        return x, y-1, "bas"
    if dir_ant == "droite":
        return x, y+1, "haut"


   
if __name__ == "__main__":
    main()