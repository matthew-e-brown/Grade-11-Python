import pygame, sys, math

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=4069)

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

pygame.display.set_caption(" .. ")

done = False
clock = pygame.time.Clock()

##Define some Fonts

CS17 = pygame.font.Font('C:/Windows/Fonts/comic.ttf', 17)

##--- Main Loop -----

boom = pygame.mixer.Sound("C:/Users/MA316BR/Downloads/Atomic_Bomb-Sound_Explorer-897730679.wav")

while not done:
    # ---
    for event in pygame.event.get():
        
        # -- VVV -- code for closing window -- VVV --
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
            ## --
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button.")
            
            mousePosX, mousePosY = pygame.mouse.get_pos()
            #print(mousePosX, "  ", mousePosY)

            #Now the higher you click, the louder the sound is
            boom.set_volume( ( (WN_HEIGHT - (int(mousePosY))) / 1000 ) )
            pygame.mixer.Sound.play(boom, loops = 0, maxtime = 0, fade_ms=0)
            ## --
        

        ## -- Game logic

        screen.fill(WHITE)


        ## -- Put drawing code here
        
        pygame.display.flip()
        
        clock.tick(60) ## FPS


pygame.quit()
