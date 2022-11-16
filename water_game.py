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
#top_left = pygame.image.load('images/top_left.png')
#top_mid = pygame.image.load('images/top_mid.png')
#top_right = pygame.image.load('images/top_right.png')
#bottom_left = pygame.image.load('images/bottom_left.png')
#bottom_mid = pygame.image.load('images/bottom_mid.png')
#bottom_right = pygame.image.load('images/bottom_right.png')

#get screen rect parameters
screen_rect = screen.get_rect()

rows = screen_rect.height // tile_size #rounds the result to the nearest whole number
cols = screen_rect.width // tile_size

coordinate = (0, 0)
def draw_background():
    #drawing my ocean on the screen
    for x in range(rows):
        for y in range(cols):
            screen.blit(water_image, (x*water_rect.height, y*water_rect.width))

    #draw my island in my ocean
    island.draw(screen)
    #screen.blit(top_left, (screen_rect.centerx - 2*tile_size, screen_rect.centery - tile_size))
    #screen.blit(top_mid, (screen_rect.centerx - tile_size, screen_rect.centery - tile_size))
    #screen.blit(top_right, (screen_rect.centerx, screen_rect.centery - tile_size ))
    #screen.blit(bottom_left, (screen_rect.centerx - 2*tile_size, screen_rect.centery))
    #screen.blit(bottom_mid, (screen_rect.centerx - tile_size, screen_rect.centery))
    #screen.blit(bottom_right, (screen_rect.centerx, screen_rect.centery))

#add a ship
my_ship = Ship()
#screen.blit(my_ship, (320, 320))

pygame.mouse.set_visible(False)
while True:
    #print("----------check for new events____________")
    recent_events = pygame.event.get()
    #print("----------done checking for events--------")
    for event in recent_events:
        if event.type == pygame.MOUSEMOTION:
            coordinate = pygame.mouse.get_pos()
            #draw_background()
            #screen.blit(my_ship, coordinate)
        if event.type == pygame.QUIT:
            #print("Ha Ha I will never quit")
            pygame.quit()
            sys.exit()

    #draw the screen
    draw_background()
    my_ship.move(coordinate)
    ship_rect = my_ship.rect
    #ship_rect.center = coordinate
    screen.blit(my_ship.image, ship_rect)
    pygame.display.flip()