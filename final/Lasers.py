import pygame


class Lasers:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.has_exploded = False
        self.image = pygame.image.load("Blue Laser.png")
        self.image.set_colorkey((255, 255, 255))
        self.hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def move(self):
        self.y -= 14
        self.hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self):
        self.y -= 14

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, enemies):
        return self.hit_box.colliderect(enemies)

