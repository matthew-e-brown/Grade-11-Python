import pygame, math, sys, time, random, os

##images and sound, as well as code created by matthew brown

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()

##Define some colours

BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
GRAY        = (230, 230, 230)
GREEN       = (10, 160, 55)
RED         = (215, 35, 35)
LIGHTRED    = (255, 60, 60)
YELLOW      = (255, 255, 255)
BLUE        = (0, 0, 255)
SKYBLUE     = (150, 215, 255)
LIGHTGREEN  = (75, 245, 125)

WN_WIDTH    = 1000
WN_HEIGHT   = 800

size    = (WN_WIDTH, WN_HEIGHT)
screen  = pygame.display.set_mode(size, 0, 32)

pygame.display.set_caption("Images and Sound Test")

clock = pygame.time.Clock()

##Define some Fonts

mainFont = pygame.font.Font('C:/Windows/Fonts/comic.ttf', 17)

##Define some Sounds

soundPEW = pygame.mixer.Sound("pew.wav")

##Define some Images

imgSHIP = pygame.image.load("ship.png").convert()
imgSHIP.set_colorkey(BLACK)

print(imgSHIP.get_rect().size)

imgBKGD = pygame.image.load("metal texture.png").convert()

##-----------------------------
## Define some game variables


## Main Game Loop:
MainGAME = True
while MainGAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            soundPEW.play()

    ship_x = int( pygame.mouse.get_pos()[0] ) - ( (imgSHIP.get_rect().size)[0])/2
    ship_y = int( pygame.mouse.get_pos()[1] ) - ( (imgSHIP.get_rect().size)[1])/1.2

    ## -- Game logic    

    ## -- Drawing code
    screen.blit(imgBKGD, [0,0])
    
    screen.blit(imgSHIP, [ship_x,ship_y])
    
    pygame.display.flip()
        
    clock.tick(60) ## FPS
