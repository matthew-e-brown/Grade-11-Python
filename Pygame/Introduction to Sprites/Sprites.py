import pygame, random, sys

BLACK       = (0,0,0)
WHITE       = (255, 255, 255)
LIGHTGRAY   = (200, 200, 200)
KEYOUT      = (1,1,1)
RED         = (170, 0, 0)
BLUE        = (66, 134, 255)

class Raindrop(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        
        super().__init__()

        ##define the internal variables for this class to be the same as the ones that were inputted
        self.color = color
        self.width = width
        self.height = height

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(KEYOUT)
        self.image.set_colorkey(KEYOUT)
        self.rect = self.image.get_rect()

        pygame.draw.rect(self.image, self.color, [0,0, self.width, self.height])

    def update(self, speed):
        if shift_pressed:
            self.rect.y += speed/10
        else:
            self.rect.y += speed
                                       
        if self.rect.y > WN_HEIGHT:
            self.rect.y = random.randrange(-100,-50)
            self.rect.x = random.randrange(WN_WIDTH)

pygame.init()

pygame.display.set_caption("Raindrop Catcher Game")

WN_WIDTH    = 1000
WN_HEIGHT   = 800

size    = (WN_WIDTH, WN_HEIGHT)
screen  = pygame.display.set_mode(size)

drops_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Raindrop(color = BLUE, width = 2, height = 25)

    block.rect.x = random.randrange(WN_WIDTH)
    block.rect.y = random.randrange(WN_HEIGHT)

    drops_list.add(block)
    all_sprites_list.add(block)

player = Raindrop(color = RED, width = 600, height = 5)
all_sprites_list.add(player)

mainGame = True

clock = pygame.time.Clock()

score = 0

## ----- main loop
shift_pressed = False
while mainGame:
    for event in pygame.event.get():
        ## quit code
        if event.type == pygame.QUIT: pygame.quit(), sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: pygame.quit(), sys.exit()
            if event.key == pygame.K_LSHIFT:
                shift_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                shift_pressed = False
        ##

    screen.fill(LIGHTGRAY)

    mouse_pos = pygame.mouse.get_pos()

    player.rect.x = int(mouse_pos[0])-(int(player.width)/2)
    player.rect.y = int(mouse_pos[1])-(int(player.height)/2)

    ##see if player has collided with anything
    drops_hit_list = pygame.sprite.spritecollide(player, drops_list, True)

    for drop in drops_hit_list:
        score += 1
        print(score)

    if len(drops_list) != 50:
        for i in range(50-(len(drops_list))):
            block = Raindrop(color = BLUE, width = 2, height = 25)

            block.rect.x = random.randrange(WN_WIDTH)
            block.rect.y = random.randrange(-100,-50)

            drops_list.add(block)
            all_sprites_list.add(block)

    drops_list.update(25)

    ##draw

    all_sprites_list.draw(screen)

    clock.tick(60)
    pygame.display.flip()

    
