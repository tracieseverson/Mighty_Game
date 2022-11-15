import pygame

class Ship:
    #create a constructor
    def __init__(self):
        self.healthy_image = pygame.image.load('images/my_ship.png')
        self.light_image = pygame.image.load('images/my_ship_light.png')
        self.heavy_image = pygame.image.load('images/my_ship_heavy.png')
        # start healthy
        self.image = self.healthy_image
        self.rect = self.image.get_rect()
        self.health = 100
        print(self.rect)

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, surface):
        if self.health < 0:
            self.image = self.light_image
        if self.health < -100:
            self.image = self.heavy_image
        surface.blit(self.image, self.rect)