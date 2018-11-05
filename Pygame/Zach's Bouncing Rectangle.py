#import pygame
import pygame
#initialize the game engine
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

#Creating a sound command
#boing = pygame.mixer.Sound("H:/Python/boing.wav") 

#defining colours 
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

RAINBOWRED = ( 255, 0, 0)
RAINBOWORANGE = ( 255, 127, 0)
RAINBOWYELLOW = ( 255, 255, 0)
RAINBOWGREEN = ( 0, 255, 0)
RAINBOWBLUE = (0, 0, 255)
RAINBOWDARKPURPLE = (75, 0, 130)
RAINBOWLIGHTPURPLE = (143, 0, 255) 

#Creating the window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame template")

# Loop until the user clicks the close button.
done = False

#Setting up rect cooridnates
rect_x = 50
rect_y = 50

#Rectangle moving vectors
rect_x_change = 5
rect_y_change = 5
gravity = 0.5

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
   
    #creates the rectangle
    pygame.draw.rect(screen, BLUE, [rect_x, rect_y, 50, 50], 0) 

    #moves the rectangle 
    rect_y_change += gravity
    rect_x += rect_x_change 
    rect_y += rect_y_change
    
    #makes the rectangle bounce back and forth.
    if rect_x > 650 or rect_x < 0:
        rect_x_change = rect_x_change * -1
        #pygame.mixer.Sound.play(boing, loops=0, maxtime=1000, fade_ms=0)

    if rect_y > 455 or rect_y < -5:
        rect_y_change = 0
        gravity = 0
        
    elif rect_y < 0:
        rect_y_change = rect_y_change * -1
        #pygame.mixer.Sound.play(boing, loops=0, maxtime=1000, fade_ms=0)
    elif rect_y > 450:
        rect_y_change = rect_y_change * -1
        #pygame.mixer.Sound.play(boing, loops=0, maxtime=1000, fade_ms=0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
