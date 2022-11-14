import pygame
import time
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
screen.fill((229, 235, 52))
pygame.display.set_caption("This is my really cool game")

while True:
    print("----------check for new events____________")
    recent_events = pygame.event.get()
    print(recent_events)
    print("----------done checking for events--------")


pygame.display.flip()
time.sleep(1)