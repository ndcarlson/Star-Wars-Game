import pygame
import random
from View import View
from EasyEnemy import Enemy
from MediumEnemy import MediumEnemy
from HardEnemy import HardEnemy
from Lasers import Lasers


class Spawn:
    def __init__(self, screen, x):
        self.screen = screen
        self.x = x
        self.spawnPoint = []

    def draw(self):
        for enemy in self.spawnPoint:
            enemy.render()
            enemy.update()

    def enemies(self):
        newEnemies = Enemy(self.screen, random.randint(30, 630), -100)
        self.spawnPoint.append(newEnemies)

    def MediumEnemies(self):
        newEnemies = MediumEnemy(self.screen, random.randint(30, 630), -100)
        self.spawnPoint.append(newEnemies)

    def HardEnemies(self):
        newEnemies = HardEnemy(self.screen, random.randint(30, 630), -100)
        self.spawnPoint.append(newEnemies)

    def remove_dead_enemy(self):
        for k in range(len(self.spawnPoint) - 1, -1, -1):
            if self.spawnPoint[k].y > self.screen.get_height() or self.spawnPoint[k].is_dead:
                del self.spawnPoint[k]
