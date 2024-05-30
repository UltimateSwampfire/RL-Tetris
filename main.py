import pygame

#Display Parameters
W , H = 10, 20
TILE_SIZE = 35
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
    
    #Update contents of entire screen
    pygame.display.flip()

    #Run program at correct FPS
    clock.tick(FPS)
