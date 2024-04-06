import sys

import pygame

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Platformer')
        self.screen = pygame.display.set_mode((640, 480)) # creates window with set resolution

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0,0,0)) # replaces color with transparency

        self.img_pos = [160, 260]
        self.movement = [False, False]; # Booleans represent if up or down key is being held

        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height()) # collision 'box' follows surface position

            if (img_r.colliderect(self.collision_area)):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 255), self.collision_area)

            # startng position [0,0] is at top left corner
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5 # Booleans convert to a 1 - True or 0 - False
            self.screen.blit(self.img, self.img_pos) # displays image on 'window'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60) # 60fps

Game().run()