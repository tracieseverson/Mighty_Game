import pygame
import sys
from ship import Ship
from island import Island

pygame.init()

water_image = pygame.image.load('images/water_image.png')
water_rect = water_image.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((10*tile_size, 10*tile_size))
pygame.display.set_caption("This is my really cool game")
screen.fill((0, 0, 0))

#load my island images
island = Island()
island.move((320, 320))

#add a ship
my_ship = Ship() #ship is now an instance (object) of the Ship class

#get screen rect parameters
screen_rect = screen.get_rect()

#get the number  of row and columns to draw by ocean background

rows = screen_rect.height // tile_size #rounds the result to the nearest whole number
cols = screen_rect.width // tile_size

coordinate = (0, 0)
def draw_background():
    #drawing my ocean on the screen
    for x in range(rows):
        for y in range(cols):
            screen.blit(water_image, (x*water_rect.height, y*water_rect.width))

pygame.mouse.set_visible(False)

while True:
    recent_events = pygame.event.get()
    for event in recent_events:
        if event.type == pygame.MOUSEMOTION:
            coordinate = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #draw the screen
    draw_background()
    island.draw(screen)
    my_ship.move(coordinate)
    ship_rect = my_ship.rect
    screen.blit(my_ship.image, ship_rect)
    pygame.display.flip()