import random
import pygame

class Enemy:
    def __init__(self, screen, x, y, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 20)
        self.is_dead = False

    def move(self):
        self.y += self.speed

    # def hit_by(self, missile):
    #     # Make a Badguy hitbox rect.
    #     # Return True if that hitbox collides with the xy point of the given missile.
    #     hitBox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
    #     return hitBox.collidepoint(missile.x, missile.y)
