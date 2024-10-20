import pygame


class Level:
    def __init__(self, screen, x):
        self.screen = screen
        self.level = 0 + x
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        levelNum = "Level: {}".format(self.level)
        levelImg = self.font.render(levelNum, True, (255, 255, 255))
        self.screen.blit(levelImg, (650, 5))