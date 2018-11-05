import pygame, sys, math, time

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

pygame.display.set_caption("Font Test")

done = False
clock = pygame.time.Clock()

##--- Main Loop -----

global keypress
keypress = 0

global timeStart
timeStart = time.time()
#timeStart = int(timeStart*100+0.5)/100

global timeEnd
timeEnd = time.time()
#timeEnd = int(timeEnd*100+0.5)/100

global elapsed

CS = pygame.font.Font('C:/Windows/Fonts/comic.ttf', 17)

while not done:
    # ---
    for event in pygame.event.get():
        
        # -- VVV -- code for closing window -- VVV --
        if event.type == pygame.QUIT:
            done = True
            
        #elif event.type == pygame.KEYDOWN:
            #print("User pressed a key.")
            ## --
            
        #elif event.type == pygame.KEYUP:
            #print("User let go of a key.")
            ## --
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print("User pressed a mouse button.")
            keypress += 1
            ## --           
        

    ## -- Game logic

    timeEnd = time.time()

    elapsed = abs(timeEnd - timeStart)
    elapsed = int(elapsed*100+0.5)/100        

    screen.fill(WHITE)

    ## -- Put drawing code here

    pygame.draw.circle(screen, SKYBLUE, (int(WN_WIDTH/4),int(WN_HEIGHT/4)), 60, 10)

    clicksText = CS.render("You've clicked " + str(keypress) + " times.", True, BLACK)
    screen.blit(clicksText,[(WN_WIDTH/2)-40,WN_HEIGHT/2])
        
    timeText = CS.render("It's taken you " + str(elapsed) + " seconds to hit that many.", True, BLACK)
    screen.blit(timeText,[(WN_WIDTH/2)-40,(WN_HEIGHT/2)+20])

    if int(elapsed) != 0:
        perSecText = CS.render("That means you click at an average of " + str(round(int(keypress) / int(elapsed),1)) + " keypresses per second.", True, BLACK)
        screen.blit(perSecText,[(WN_WIDTH/2)-40,(WN_HEIGHT/2)+40])
    else:
        perSecText = CS.render("...", False, BLACK)
        screen.blit(perSecText,[(WN_WIDTH/2)-40,(WN_HEIGHT/2)+40])
        
    pygame.display.flip()
        
    #clock.tick(60) ## FPS


pygame.quit()
