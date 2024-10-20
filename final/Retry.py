import pygame


class Retry:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("final/Retry.jpg")
        # self.fire_sound = pygame.mixer.Sound("")

    def render(self):
        # Make each badguy in this EnemyFleet draw itself.
        self.screen.blit(self.image, (self.x, self.y))
