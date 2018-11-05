import pygame, math, sys, time, random, os, pygame.gfxdraw

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()

##Define some colours

BLACK       = (0, 0, 0)
KEYOUT      = (1, 1, 1)
WHITE       = (255, 255, 255)
LIGHTGRAY   = (230, 230, 230)
DARKGRAY    = (70, 70, 70)
GREEN       = (10, 160, 55)
RED         = (215, 35, 35)
LIGHTGREEN  = (75, 245, 125)
LIGHTRED    = (255, 60, 60)
DARKRED     = (153, 0, 0)
YELLOW      = (255, 242, 0)
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

class Pac(pygame.sprite.Sprite):
    def __init__(self, startposx, startposy):

        super().__init__()
        
        self.size = 96
        self.color = YELLOW
        self.speed = 4

        self.image = pygame.image.load("Pacman Sequence.bmp").convert()
        self.image.set_colorkey(KEYOUT)
        self.rect = self.image.get_rect()  

    def move(self):
        
        if shift_pressed:
            if up: self.rect.y -= self.speed * 3
            if down: self.rect.y += self.speed * 3
            if left: self.rect.x -= self.speed * 3
            if right: self.rect.x += self.speed * 3
        else:
            if up: self.rect.y -= self.speed
            if down: self.rect.y += self.speed
            if left: self.rect.x -= self.speed
            if right: self.rect.x += self.speed

        

## Define some Variables
all_sprites_list = pygame.sprite.Group()

pacman = Pac(80, 80)
all_sprites_list.add(pacman)

up = False
down = False
left = False
right = False
shift_pressed = False

## Main Game Loop:
MainGAME = True
while MainGAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: up = True
            if event.key == pygame.K_s: down = True
            if event.key == pygame.K_a: left = True
            if event.key == pygame.K_d: right = True
            
            if event.key == pygame.K_LSHIFT: shift_pressed = True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: up = False
            if event.key == pygame.K_s: down = False
            if event.key == pygame.K_a: left = False
            if event.key == pygame.K_d: right = False

            if event.key == pygame.K_LSHIFT: shift_pressed = False
            
                    
    ## -- Game logic

    screen.fill(LIGHTGRAY)
    
    pacman.move()

    ## -- Drawing code
    
    all_sprites_list.draw(screen)
    pygame.display.flip()
        
    clock.tick(60) ## FPS
