import pygame

class Island:
    #create a constructor

    def __init__(self):
        self.image = pygame.image.load('images/bottom_left.png')
        self.rect = self.image.get_rect()

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, surface):
        surface.blit(self.image, self.rect)