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

#draw the background
def draw_background():
    for x in range(rows):
        for y in range(cols):
            screen.blit(water_image, (x*water_rect.height, y*water_rect.width))

    #add an island
    #load all the island images
    island_bottom_left = pygame.image.load('images/island_bottom_left.png')
    island_bottom_mid = pygame.image.load('images/island_bottom_mid.png')
    island_bottom_right = pygame.image.load('images/island_bottom_right.png')
    island_top_left = pygame.image.load('images/island_top_left.png')
    island_top_mid = pygame.image.load('images/island_top_mid.png')
    island_top_right = pygame.image.load('images/island_top_right.png')

    #blit them to the screen
    #screen.blit(island_top_left, (tile_size, 0))
    #screen.blit(island_top_mid, (tile_size*2, 0))
    #screen.blit(island_top_right, (tile_size*3, 0))
    #screen.blit(island_bottom_left, (tile_size, tile_size))
    #screen.blit(island_bottom_mid, (tile_size*2, tile_size))
    #screen.blit(island_bottom_right, (tile_size*3, tile_size))

    #what if I wanted it in the center of my screen?
    screen_rect = screen.get_rect()
    print(screen_rect.center)
    screen.blit(island_top_left, (screen_rect.centerx - 2*tile_size, screen_rect.centery - tile_size))
    screen.blit(island_top_mid, (screen_rect.centerx-tile_size, screen_rect.centery - tile_size))
    screen.blit(island_top_right, (screen_rect.centerx, screen_rect.centery - tile_size))
    screen.blit(island_bottom_left, (screen_rect.centerx - 2*tile_size, screen_rect.centery))
    screen.blit(island_bottom_mid, (screen_rect.centerx-tile_size, screen_rect.centery))
    screen.blit(island_bottom_right, (screen_rect.centerx, screen_rect.centery))

#add a ship
my_ship = pygame.image.load('images/my_ship.png')
#screen.blit(my_ship, (50, 50))
#screen.blit(my_ship, (500, 500))

while True:
    #print("----------check for new events____________")
    recent_events = pygame.event.get()
    #print("----------done checking for events--------")
    for event in recent_events:
        if event.type == pygame.MOUSEMOTION:
            print(type(event.pos))
            coordinate = pygame.mouse.get_pos()
            #screen.blit(my_ship, coordinate)
            #screen.blit(my_ship, event.pos)
        if event.type == pygame.QUIT:
            #print("Ha Ha I will never quit")
            pygame.quit()
            sys.exit()

    #draw the screen
    draw_background()
    screen.blit(my_ship, coordinate)
    pygame.display.flip()