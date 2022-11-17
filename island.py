import pygame

class Island:
    #create island constructor
    def __init__(self):
        #self.image = pygame.image.load('images/top_left.png')
        #self.rect = self.image.get_rect()

        self.image = pygame.surface.Surface((192, 128))
        self.image.blit(pygame.image.load('images/water_image.png'), (0, 0))
        self.image.blit(pygame.image.load('images/top_left.png'), (0, 0))
        self.image.blit(pygame.image.load('images/water_image.png'), (64, 0))
        self.image.blit(pygame.image.load('images/top_mid.png'), (64, 0))
        self.image.blit(pygame.image.load('images/water_image.png'), (128, 0))
        self.image.blit(pygame.image.load('images/top_right.png'), (128, 0))
        self.image.blit(pygame.image.load('images/water_image.png'), (0, 64))
        self.image.blit(pygame.image.load('images/bottom_left.png'), (0, 64))
        self.image.blit(pygame.image.load('images/water_image.png'), (64, 64))
        self.image.blit(pygame.image.load('images/bottom_mid.png'), (64, 64))
        self.image.blit(pygame.image.load('images/water_image.png'), (128, 64))
        self.image.blit(pygame.image.load('images/bottom_right.png'), (128, 64))
        self.rect = self.image.get_rect()


    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, surface):
        surface.blit(self.image, self.rect)