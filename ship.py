import pygame

class Ship:
    #create a constructor
    def __init__(self):
        self.image = pygame.image.load('images/my_ship.png')
        self.rect = self.image.get_rect()
        print(self.rect)

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, surface):
        surface.blit(self.image, self.rect)