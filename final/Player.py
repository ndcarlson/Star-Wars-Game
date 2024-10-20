import pygame
from Lasers import Lasers


class Player:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('final/NicePng_fairy-wings-side-view_2150322.png')
        self.rectPlayerimg = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.lasers = []
        self.reload = 0
        self.is_dead = False
        self.hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self, newX, newY):
        self.x = newX
        self.y = newY

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        self.reload += 1
        laser_image = pygame.image.load("final/Blue Laser.png")
        left_lasers = Lasers(self.screen, self.x - laser_image.get_width() // 2 + 4, self.y + 10)
        right_lasers = Lasers(self.screen, self.x + self.image.get_width() - laser_image.get_width() // 2 - 4, self.y + 10)
        self.lasers.append(left_lasers)
        self.lasers.append(right_lasers)

    def hit_by(self, spawnPoint):
        hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return hit_box.colliderect(spawnPoint.hit_box)

    def remove_exploded_lasers(self):
        for k in range(len(self.lasers) - 1, -1, -1):
            if self.lasers[k].has_exploded or self.lasers[k].y < 0:
                del self.lasers[k]

