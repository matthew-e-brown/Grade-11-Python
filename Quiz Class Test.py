import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self, INpos_x, INpos_y, INname, INstrength):

        super().__init__()
        self.image = pygame.Surface([52, 55])
        self.image = pygame.image.load("link.png")
        self.image.set_colorkey(KEYOUT) #color set earlier in the program to key out, letting BLACK stay used. Equal to (1,1,1)
        self.rect = self.image.get_rect()

        ##IN = short for Input
        self.rect.x = INpos_x
        self.rect.y = INpos_y

        self.name = INname
        self.strength = INstrength

        screen.blit(screen, self.image)

    def attack(self, force):
        print(self.name, "attacked and dealt", int(self.strength) * force, "damage!")

goodguy = Hero(30, 0, "Link", 130)
goodguy.attack(12)
