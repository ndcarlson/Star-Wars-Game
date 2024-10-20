from random import random

import pygame
from Player import Player
from EasyEnemy import Enemy
from MediumEnemy import MediumEnemy
from Boss import Boss
from StartScreen import Start
from HardEnemy import HardEnemy
from Ammo import Ammo

import pygame
import random

# done: Nicholas and Jacob


class Game:
    def __init__(self, screen: pygame.Surface):
        self.enemy = Enemy(screen, random.randint(150, 750), -100)
        self.mediumEnemy = MediumEnemy(screen, random.randint(50, 630), -100)
        self.screen = screen
        self.player = Player(screen, screen.get_width() // 2 - 60, screen.get_height() - 400)
        self.tutorialShip = Player(screen, 450, 200)
        self.hardEnemy = HardEnemy(screen, random.randint(150, 750), -100)
        self.start = Start(screen, 0, 0)
        self.ammo = Ammo(screen)



    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        # self.player.draw()
        # self.enemy.draw()
        # Use something like the following, but for the objects in YOUR game:
        #     self.fighter.draw()
        #     self.missiles.draw()
        #     self.enemies.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # Use something like the following, but for the objects in YOUR game:
        #     self.missiles.move()
        #     self.enemies.move()
        #     self.missiles.handle_explosions(self.enemies)
