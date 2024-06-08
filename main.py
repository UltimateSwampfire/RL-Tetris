import pygame
import random
from coordinates import *
#Display Parameters
W , H = 10, 20
TILE_SIZE = 40
GAME_RES = (W * TILE_SIZE, H * TILE_SIZE)
FPS = 60

#Initialize all pygame modules (Getting Ready)
pygame.init()

#Initalize a display window of size GAME_RES
game_sc = pygame.display.set_mode(size = GAME_RES)

#Create a clock instance
clock = pygame.time.Clock()

#List of grid-block items
grid = [pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE) for x in range(W) for y in range(H)]

#Figures
figures = [[pygame.Rect(x + W//2,y+3,1,1) for x,y in figure] for figure in figures_pos]
#Template Rectangle
figure_rect = pygame.Rect(0,0,TILE_SIZE-2,TILE_SIZE-2)
#Sample Piece
n = random.randint(0,6)
try:
    while True:
        #Fill background color of display window
        game_sc.fill(color = pygame.Color("Black"))

        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        #Draw a grid
        for gridblock in grid:
            pygame.draw.rect(surface = game_sc, color = (50,50,50), rect = gridblock, width = 1)

        #TODO : Controls aren't responsive. It gets better only with better FPS.
        #Controls
        dx = 0
        dy = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1
                elif event.key == pygame.K_UP:
                    dy = -1
                elif event.key == pygame.K_DOWN:
                    dy = 1

        
        #Moving Horizontally
        for i in range(4):
            figures[n][i].x += dx
            figures[n][i].y += dy


        for i in range(4):
            figure_rect.x = figures[n][i].x * TILE_SIZE
            figure_rect.y = figures[n][i].y * TILE_SIZE
            pygame.draw.rect(game_sc,colors[n],figure_rect)


        #Update contents of entire screen
        pygame.display.flip()

        #Run program at correct FPS
        clock.tick(FPS)

except KeyboardInterrupt:
    pass

