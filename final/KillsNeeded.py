import pygame


class KillsNeeded:
    def __init__(self, screen, x):
        self.screen = screen
        self.level = 0 + x
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        Kills = "Kills Needed: {}".format(self.level)
        killsImg = self.font.render(Kills, True, (255, 255, 255))
        self.screen.blit(killsImg, (590, 780))