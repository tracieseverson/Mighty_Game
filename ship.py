import pygame

class Ship:
    #create ship constructor
    def __init__(self):
        self.healthy_image = pygame.image.load('images/my_ship.png')
        self.light_image = pygame.image.load('images/light_damage.png')
        self.heavy_image = pygame.image.load('images/heavy_damage.png')
        self.destroyed_image = pygame.image.load('images/destroyed.png')
        self.image = self.healthy_image
        self.rect = self.image.get_rect()
        self.health = 100

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, surface):
        if self.health <= 0:
            self.image = self.light_image
        if self.health <= -100:
            self.image = self.heavy_image
        if self.health <= -200:
            self.image = self.destroyed_image
        surface.blit(self.image, self.rect)