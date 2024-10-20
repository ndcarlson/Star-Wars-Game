import pygame


class Start:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("load screen.png")

    def render(self):
        # if self.y < self.screen.get_height() - 300:
        self.screen.blit(self.image, (self.x, self.y))
