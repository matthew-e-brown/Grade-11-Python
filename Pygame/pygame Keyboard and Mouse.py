import pygame, math, sys, time, random

pygame.init()

##Define some colours

BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
LIGHTGRAY   = (230, 230, 230)
DARKGRAY    = (70, 70, 70)
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
screen  = pygame.display.set_mode(size)

pygame.display.set_caption("Keyboard and Mouse at the Same Time")

clock = pygame.time.Clock()

##Define some Fonts

mainFont = pygame.font.Font('C:/Windows/Fonts/comic.ttf', 17)

##Define some Sounds

##-----------------------------
## Define some game variables
sqSize = 52
sqPosX = WN_WIDTH/2 + sqSize/2
sqPosY = WN_HEIGHT/2 + sqSize/2

w_pressed = False
a_pressed = False
s_pressed = False
d_pressed = False
shift = False

explainText1 = mainFont.render("Hold shift to walk instead of run!", True, BLACK)

## Main Game Loop:
while True:

    speed = 10
    mouseX, mouseY = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                w_pressed = True
            elif event.key == pygame.K_a:
                a_pressed = True
            elif event.key == pygame.K_s:
                s_pressed = True
            elif event.key == pygame.K_d:
                d_pressed = True

            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shift = True
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                w_pressed = False
            elif event.key == pygame.K_a:
                a_pressed = False
            elif event.key == pygame.K_s:
                s_pressed = False
            elif event.key == pygame.K_d:
                d_pressed = False

            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shift = False

    if shift:
        speed = speed/2

    if sqPosY > 0:
        if w_pressed:
            sqPosY -= speed
    if sqPosY < (WN_HEIGHT- sqSize):    
        if s_pressed:
            sqPosY += speed
    if sqPosX > 0:    
        if a_pressed:
            sqPosX -= speed
    if sqPosX < (WN_WIDTH - sqSize):   
        if d_pressed:
            sqPosX += speed
        
    ## -- Game logic

    

    ## -- Put drawing code here
    screen.fill(LIGHTGRAY)
    screen.blit(explainText1, [300,300])
    pygame.draw.rect(screen, DARKGRAY, [sqPosX, sqPosY, sqSize, sqSize])
    pygame.draw.ellipse(screen, LIGHTGREEN, [(mouseX-(sqSize/2)),(mouseY-(sqSize/2)), sqSize, sqSize])
    pygame.display.flip()
        
    clock.tick(60) ## FPS
