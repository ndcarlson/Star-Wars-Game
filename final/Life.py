import pygame


class Life:
    def __init__(self, screen, x):
        self.screen = screen
        self.level = 0 + x
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        life = "Lives: {}".format(self.level)
        lifeImg = self.font.render(life, True, (255, 255, 255))
        self.screen.blit(lifeImg, (5, 780))