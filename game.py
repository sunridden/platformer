import sys

import pygame

pygame.init()

pygame.display.set_caption('Platformer')

screen = pygame.display.set_mode((640, 480)) # creates window with resolution

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60) # 60fps