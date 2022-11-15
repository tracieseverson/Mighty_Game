import pygame
import sys
from ship import Ship

pygame.init()

water_image = pygame.image.load('images/water_image.png')
water_rect = water_image.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((10*tile_size, 10*tile_size))
pygame.display.set_caption("This is my really cool game")
screen.fill((0, 0, 0))

#load my island images
top_left = pygame.image.load('images/top_left.png')
top_mid = pygame.image.load('images/top_mid.png')
top_right = pygame.image.load('images/top_right.png')
bottom_left = pygame.image.load('images/bottom_left.png')
bottom_mid = pygame.image.load('images/bottom_mid.png')
bottom_right = pygame.image.load('images/bottom_right.png')

#add a ship
my_ship = Ship() #ship is now an object that *has* a surface

#get screen rect parameters
screen_rect = screen.get_rect()

rows = screen_rect.height // tile_size #rounds the result to the nearest whole number
cols = screen_rect.width // tile_size

def draw_background():
    #drawing my ocean on the screen
    for x in range(rows):
        for y in range(cols):
            screen.blit(water_image, (x*water_rect.height, y*water_rect.width))

    #draw my island in my ocean
    screen.blit(top_left, (screen_rect.centerx - 2*tile_size, screen_rect.centery - tile_size))
    screen.blit(top_mid, (screen_rect.centerx - tile_size, screen_rect.centery - tile_size))
    screen.blit(top_right, (screen_rect.centerx, screen_rect.centery - tile_size ))
    screen.blit(bottom_left, (screen_rect.centerx - 2*tile_size, screen_rect.centery))
    screen.blit(bottom_mid, (screen_rect.centerx - tile_size, screen_rect.centery))
    screen.blit(bottom_right, (screen_rect.centerx, screen_rect.centery))

coordinate = (0, 0)

while True:
    recent_events = pygame.event.get()
    for event in recent_events:
        if event.type == pygame.MOUSEMOTION:
            coordinate = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #update the ship
    my_ship.move(coordinate)

    # draw the screen
    draw_background()
    my_ship.draw(screen)
    #screen.blit(my_ship.image, my_ship.rect)
    pygame.display.flip()