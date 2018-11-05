import pygame, sys, math

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

pygame.display.set_caption(" .. ")

done = False
clock = pygame.time.Clock()

##--- Main Loop -----

while not done:
    # ---
    for event in pygame.event.get():
        
        # -- VVV -- code for closing window -- VVV --
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
            ## --
            
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
            ## --
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button.")
            ## --
        

        ## -- Game logic

        screen.fill(WHITE)

        ## -- Put drawing code here
        pygame.draw.rect(screen, SKYBLUE, [50,50,200,200])
        pygame.draw.line(screen, LIGHTGREEN, [50,50], [250,250],5)

        ## -- Series of lines

        for y_offset in range(0,800,25):
            pygame.draw.line(screen,BLACK,[0,0+y_offset],[WN_WIDTH,0+y_offset],5)
        
        pygame.display.flip()
        
        clock.tick(60) ## FPS


pygame.quit()
