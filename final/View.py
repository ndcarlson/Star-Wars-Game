import pygame
from Game import Game

# done: Nicholas and Jacob


class View:
    def __init__(self, screen: pygame.Surface, game: Game):
        self.screen = screen
        self.game = game
        self.background_color = pygame.Color("black")  # TODO: Choose your own color

    def draw_everything(self):
        self.screen.fill(self.background_color)
        self.game.draw_game()  # TODO: Implement draw_game in your Game
        pygame.display.update()
