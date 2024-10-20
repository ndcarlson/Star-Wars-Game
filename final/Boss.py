import sys
import time
import pygame
import math


class Boss:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("final/Medium Enemy.png")
        self.image.set_colorkey((255, 255, 255))
        self.rectBGimg = self.image.get_rect()

        xscale = 2 / (3 - math.cos(2 * x))
        yscale = 2 / (3 - math.cos(2 * y))

        self.x = 325
        self.y = 50

        self.speedY = 10
        self.speedX = 10

    def move(self):
        self.y += self.speedY
        self.x += self.speedX

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def update(self):
        if self.y > 300 or self.y < 10:
            self.y -= self.speedY
        else:
            self.y += self.speedY

        if self.x > 650 or self.x < 100:
            self.x -= self.speedX
        if self.x <= 650 or self.x >= 100:
            self.x += self.speedX

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))
