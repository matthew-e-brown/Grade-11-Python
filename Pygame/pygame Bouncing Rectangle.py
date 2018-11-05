import pygame, math, sys, time

pygame.init()

##Define some colours

BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
GREEN       = (0, 255, 0)
RED         = (255, 0, 0)
YELLOW      = (255, 255, 255)
BLUE        = (0, 0, 255)
SKYBLUE     = (150, 215, 255)
LIGHTGREEN  = (75, 245, 125)

WN_WIDTH    = 1000
WN_HEIGHT   = 800

size    = (WN_WIDTH, WN_HEIGHT)
screen  = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing Rectangle")

clock = pygame.time.Clock()

##Define some Fonts

CS17 = pygame.font.Font('C:/Windows/Fonts/comic.ttf', 17)

##Define some Sounds

#boing1 = pygame.mixer.Sound("C:/Users/MA316BR/Downloads/159376__greenhourglass__boing1.wav")
#boing1.set_volume(0.3)

#def soundBoing():
    #pygame.mixer.Sound.play(boing1, loops = 0, maxtime = 0, fade_ms = 0)

##-------------------------
## Rectangle Size
rectSizeX, rectSizeY = (75, 75)

## Rectangle starting pos
rect_x, rect_y = (50, 50)

## Rect change amount
rectChangeX, rectChangeY = (5, 5)

## Gravity
grav = 0.5
slide = 0.5

##--- Main Loop -----

pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=4069)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), sys.exit()
    
    rectChangeY += grav

    if grav == 0:
        rectChangeX += slide
    
    rect_x += rectChangeX
    rect_y += rectChangeY
    
    if rect_y > ((WN_HEIGHT - rectSizeY)+13) or rect_y < 13:
        grav = 0
        rectChangeY = 0
        testText = CS17.render("TEST, You're supposed to have stopped by now // Y", True, BLACK)
        screen.blit(testText, [0,0])
        
    elif rect_y > (WN_HEIGHT - rectSizeY) or rect_y < 0:
        #soundBoing()
        rectChangeY = rectChangeY * (-1)

    if rect_x > ((WN_WIDTH - rectSizeX) + 13) or rect_x < -12:
        slide = 0
        rectChangeX = 0
        testText = CS17.render("TEST, You're supposed to have stopped by now // X", True, BLACK)
        screen.blit(testText, [0,0])
        
    elif rect_x > (WN_WIDTH - rectSizeX) or rect_x < 0:
        #soundBoing()
        rectChangeX = rectChangeX * (-1)

    ## Draw the rect, my boyyo
    screen.fill(WHITE)
    pygame.draw.rect(screen, SKYBLUE, [rect_x, rect_y, rectSizeX, rectSizeY])
    
    clock.tick(100)
    pygame.display.flip() ## FPS

