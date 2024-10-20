import pygame


class Ammo:
    def __init__(self, screen):
        self.screen = screen
        self.ammo = 100
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        ammo_string = "Ammo: {}".format(self.ammo)
        ammo_image = self.font.render(ammo_string, True, (255, 255, 255))
        self.screen.blit(ammo_image, (5, 5))