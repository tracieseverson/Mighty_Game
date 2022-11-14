import pygame
import sys

pygame.init()

water_image = pygame.image.load('images/water_image.png')
water_rect = water_image.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((10*tile_size, 10*tile_size))
pygame.display.set_caption("This is my really cool game")
screen.fill((0, 0, 0))

screen_rect = screen.get_rect()

rows = screen_rect.height//tile_size #rounds the result to the nearest whole number
cols = screen_rect.width//tile_size

for x in range(rows):
    for y in range(cols):
        screen.blit(water_image, (x*water_rect.height, y*water_rect.width))

while True:
    #print("----------check for new events____________")
    recent_events = pygame.event.get()
    #print("----------done checking for events--------")
    for event in recent_events:
        if event.type == pygame.QUIT:
            #print("Ha Ha I will never quit")
            pygame.quit()
            sys.exit()

    #draw the screen
    pygame.display.flip()