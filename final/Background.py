import pygame
from View import View
from EasyEnemy import Enemy


class Background:
    def __init__(self, screen):
        self.screen = screen
        self.bgimage = pygame.image.load("final/deathStarLayout,Dark.jpg")
        self.rectBGimg = self.bgimage.get_rect()

        self.backGroundX1 = 0
        self.backGroundY1 = 0

        self.backGroundY2 = 0 - self.rectBGimg.height
        self.backGroundX2 = 0

        self.moving_speed = 5

    def update(self):
        self.backGroundY1 += self.moving_speed
        self.backGroundY2 += self.moving_speed
        if self.backGroundY1 >= self.rectBGimg.height:
            self.backGroundY1 = -self.rectBGimg.height
        if self.backGroundY2 >= self.rectBGimg.height:
            self.backGroundY2 = -self.rectBGimg.height

    def render(self):
        self.screen.blit(self.bgimage, (self.backGroundX1, self.backGroundY1))
        self.screen.blit(self.bgimage, (self.backGroundX2, self.backGroundY2))