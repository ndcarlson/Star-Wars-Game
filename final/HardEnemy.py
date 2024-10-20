import pygame
import random


class HardEnemy:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.is_dead = False
        self.image = pygame.image.load("final/star-wars-tie-advanced-x1-drone.png")
        self.rectPlayerimg = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.speed = random.randint(5, 15)
        self.hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.life = 30

    def hit_by(self, lasers):
        return self.hit_box.colliderect(lasers.hit_box)

    def update(self):
        self.y = self.y + self.speed
        self.hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y - 10,
                                                    self.image.get_width(), 5))
        pygame.draw.rect(self.screen, (0, 128, 0), (self.x, self.y - 10,
                                                    self.image.get_width(), 5))


