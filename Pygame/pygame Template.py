import pygame, math, sys, time, random, os, pygame.gfxdraw

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()

##Define some colours

BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
LIGHTGRAY   = (230, 230, 230)
DARKGRAY    = (70, 70, 70)
GREEN       = (10, 160, 55)
RED         = (215, 35, 35)
LIGHTGREEN  = (75, 245, 125)
LIGHTRED    = (255, 60, 60)
DARKRED     = (153, 0, 0)
YELLOW      = (255, 230, 35)
BLUE        = (0, 0, 255)
SKYBLUE     = (150, 215, 255)

WN_WIDTH    = 1000
WN_HEIGHT   = 800

size    = (WN_WIDTH, WN_HEIGHT)
screen  = pygame.display.set_mode(size, 0, 32)

pygame.display.set_caption("Template")

clock = pygame.time.Clock()

##Define some Fonts

mainFont = pygame.font.Font('C:/Windows/Fonts/comic.ttf', 17)

##Define some Sounds

##Define some Classes

## Define some Variables


## Main Game Loop:
MainGAME = True
while MainGAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), sys.exit()

    ## -- Game logic
        

    

    ## -- Drawing code
    screen.fill(WHITE)
    
    pygame.display.flip()
        
    clock.tick(60) ## FPS
