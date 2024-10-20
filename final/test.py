import random
import sys
import time
import math

import pygame
from Background import Background
from Game import Game
from Controller import Controller
from View import View
from Player import Player
from EasyEnemy import Enemy
from Spawn import Spawn
from Boss import Boss

# done: Put your names here (Nicholas Carlson, Jacob Scheibe)


def main():
    pygame.init()
    screen = pygame.display.set_mode((750, 800))  # done: Choose your own size
    bg = Background(screen)
    Xwing = Player(screen)
    TiFigter = EasyEnemy(screen, random.randint(50, 630), -100)
    spawn = Spawn(screen, random.randint(30, 630))
    boss = Boss(screen, 350, 100)

    clock = pygame.time.Clock()
    currentTime = 0
    buttonPressTime  = 0
    count = 0
    run = ''

    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game)  # the Controller

    isGameOver = False

    frame_rate = 30  # done: Choose your own frame rate

    while True:
        clock.tick(frame_rate)

        controller.get_and_handle_events()
        game.run_one_cycle()
        viewer.draw_everything()

        count = count + 1
        print(count)

        print(spawn.spawnPoint)

        # spawn.enemies()
        # spawn.draw()

        if count > 20:
            count = 0
            spawn.EasyEnemy()
            run = 'yes'

        TiFigter.offScreen()
        if TiFigter.offScreen:
            print('helklo')
            spawn.remove_dead_enemy()

        #     for enemie in spawn.spawnPoint:
        #         enemie.move()
        #         enemie.draw()
        #
        #         TiFigter.render()
        #         TiFigter.update(game.enemy.x, game.enemy.y)
        #
                # if len(spawn.spawnPoint > 0) and TiFigter.offScreen():
                #     spawn.spawnPoint.remove(enemie)

        # if not TiFigter.is_dead:
        #     TiFigter.render()
        #     TiFigter.update(game.enemy.x, game.enemy.y)
        #     # if len(spawn.spawnPoint > 0) and TiFigter.offScreen():
        #     #     spawn.spawnPoint.remove(Enemy)
        # if run == 'yes':
        #     spawn.draw()

            # spawn.spawnPoint.remove()

        if TiFigter.offScreen():
            TiFigter.is_dead = True

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and game.player.x + game.player.image.get_width() / 2 > 0:
            game.player.x -= 10
        if pressed_keys[pygame.K_RIGHT] and game.player.x < \
                game.screen.get_width() - game.player.image.get_width() / 2:
            game.player.x += 10
        if pressed_keys[pygame.K_UP] and game.player.y > 0:
            game.player.y -= 10
        if pressed_keys[pygame.K_DOWN] and game.player.y < \
                game.screen.get_height() - game.player.image.get_height() * (3 / 4):
            game.player.y += 10
        if pressed_keys[pygame.K_ESCAPE]:
            sys.exit()
        if pressed_keys[pygame.K_SPACE]:
            game.player.fire()

        for lasers in game.player.lasers:
            lasers.move()
            lasers.draw()

            # for enemie in spawn.spawnPoint:
            #     enemie.move()
            #     enemie.draw()
            #
            #     #
            #     # TiFigter.render()
            #     # TiFigter.update(game.enemy.x, game.enemy.y)
            #     #
            #     # if TiFigter.offScreen():
            #     #     spawn.spawnPoint.remove(enemie)

        spawn.draw()

        # bg.update()
        # bg.render()

        # boss.render()
        # boss.update()

        Xwing.render()
        Xwing.update(game.player.x, game.player.y)

        # TiFigter.render()
        # TiFigter.update(game.enemy.x, game.enemy.y)
        # if TiFigter.offScreen():
        #     TiFigter.is_dead = True
        #     spawn.spawnPoint.remove(Enemy)

        pygame.display.update()

main()
