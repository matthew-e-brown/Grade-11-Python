import pygame, math, sys, time, random

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

##-----------------------------
## Define some game variables

snowlist = []

for i in range(50):
    x = random.randrange(0,WN_WIDTH)
    y = random.randrange(0,WN_HEIGHT)
    snowlist.append([x,y])

## Main Game Loop:
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), sys.exit()        

    screen.fill(BLACK)
        
    for i in range(len(snowlist)):
        pygame.draw.circle(screen, WHITE, snowlist[i], 2)

        snowlist[i][1] += int(9.1)

        if snowlist[i][1] > WN_HEIGHT:
            y = random.randrange(-50, -10)
            snowlist[i][1] = y
            x = random.randrange(0,WN_WIDTH)
            snowlist[i][0] = x
        
    pygame.display.flip()
    
        
    clock.tick(60) ## FPS


pygame.quit()
