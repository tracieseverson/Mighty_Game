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

boom = pygame.mixer.Sound('boom.mp3')

#load my island images
island = Island()
island.move((320, 320))

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


coordinate = (0, 0)

clock = pygame.time.Clock()
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
    #determine collisions
    collision = pygame.sprite.collide_rect(my_ship, island)
    if collision:
        print(f"You just ran into the Island!: Your ship health is {my_ship.health}")
        pygame.mixer.Sound.play(boom)
        my_ship.health = my_ship.health - 1

    # draw the screen
    draw_background()
    # draw my island in my ocean
    island.draw(screen)
    my_ship.draw(screen)
    #screen.blit(my_ship.image, my_ship.rect)
    pygame.display.flip()
    clock.tick(60)