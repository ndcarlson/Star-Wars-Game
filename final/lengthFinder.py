import pygame

class Length:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("final/dimensionFinder.png")
        self.image.set_colorkey((255, 255, 255))
        # self.fire_sound = pygame.mixer.Sound("")

    def render(self):
        # Make each badguy in this EnemyFleet draw itself.
        self.screen.blit(self.image, (self.x, self.y))
