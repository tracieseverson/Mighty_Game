import pygame

class Ship:
    #create ship constructor
    def __init__(self):
        self.image = pygame.image.load('images/my_ship.png')
        self.rect = self.image.get_rect()

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, surface):
        surface.bilt(self.image, self.rect)