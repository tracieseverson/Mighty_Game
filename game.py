import pygame
import time
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("This is my really cool game")
screen.fill((0, 0, 255))

while True:
    print("----------check for new events____________")
    recent_events = pygame.event.get()
    print(recent_events)
    print("----------done checking for events--------")
    for event in recent_events:
        if event.type == pygame.QUIT:
            print("Ha Ha I will never quit")
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill((255, 0, 0))
            elif event.key == pygame.K_g:
                screen.fill((0, 255, 0))
            elif event.key == pygame.K_b:
                screen.fill((0, 0, 255))
    pygame.display.flip()
    time.sleep(1)

