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
from MediumEnemy import MediumEnemy
from StartScreen import Start
from Menu import Menu
from lengthFinder import Length
from Tutorial import Tutorial
from HardEnemy import HardEnemy
from Lasers import Lasers
from Ammo import Ammo
from level import Level
from Retry import Retry
from KillsNeeded import KillsNeeded
from Life import Life

# done: Nicholas Carlson, Jacob Scheibe


def main():
    pygame.init()
    screen = pygame.display.set_mode((750, 800))  # done: Choose your own size
    bg = Background(screen)
    tutorialShip = Player(screen, 0, 0)
    spawn = Spawn(screen, random.randint(30, 630))
    start = Start(screen, 0, 0)
    menu = Menu(screen, 0, 0)
    tutorial = Tutorial(screen, 0, 0)
    dimension = Length(screen, 261, 760)
    restart = Retry(screen, 0, 0)

    clock = pygame.time.Clock()
    EasySpawnTimer = 0
    MediumSpawnTimer = 0
    HardSpawnTimer = 0

    retry = True
    count = 0
    level = 1
    x = 0
    tutorialCheck = 0
    death_count = 0
    killCount = 0

    full_ammo = 100
    ammo = 100
    reload_time = 1.2
    reloading = False
    outOfAmmo = False
    lastReloadTime = 0
    cont = True
    menu1 = True
    origionalHearts = 4

    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game)  # the Controller

    frame_rate = 30  # done: Choose your own frame rate

    while x == 0:
        start.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = 1
        pygame.display.update()


    while True:
        retry = True
        menu.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickPos = event.pos
                if 237 < clickPos[0] < 492 and 582 < clickPos[1] < 692:
                    sys.exit()
                if 237 < clickPos[0] < 492 and 155 < clickPos[1] < 582:
                    while tutorialCheck == 0:

                        tutorial.render()

                        pressed_keys = pygame.key.get_pressed()
                        if reloading and time.time() - lastReloadTime > reload_time:
                            reloading = False
                        if reloading is False and outOfAmmo is False and pressed_keys[pygame.K_SPACE] and ammo > 0:
                            ammo -= 1
                            print(ammo)
                            tutorialShip.fire()
                        if ammo == 0:
                            outOfAmmo = True
                        if pressed_keys[pygame.K_RSHIFT] or pressed_keys[pygame.K_LSHIFT]:
                            lastReloadTime = time.time()
                            reloading = True
                            outOfAmmo = False
                            ammo = full_ammo

                        for lasers in tutorialShip.lasers:
                            lasers.move()
                            lasers.draw()

                        game.tutorialShip.remove_exploded_lasers()

                        tutorialShip.render()
                        tutorialShip.update(game.tutorialShip.x, game.tutorialShip.y)

                        pressed_keys = pygame.key.get_pressed()
                        if pressed_keys[pygame.K_LEFT] and game.tutorialShip.x + game.tutorialShip.image.get_width() / 2 > 0:
                            game.tutorialShip.x -= 13
                        if pressed_keys[pygame.K_RIGHT] and game.tutorialShip.x < \
                                game.screen.get_width() - game.tutorialShip.image.get_width() / 2:
                            game.tutorialShip.x += 13
                        if pressed_keys[pygame.K_UP] and game.tutorialShip.y > 0:
                            game.tutorialShip.y -= 13
                        if pressed_keys[pygame.K_DOWN] and game.tutorialShip.y < \
                                game.screen.get_height() - game.tutorialShip.image.get_height() * (3 / 4):
                            game.tutorialShip.y += 13
                        if pressed_keys[pygame.K_ESCAPE]:
                            sys.exit()
                        if pressed_keys[pygame.K_SPACE]:
                            game.tutorialShip.fire()

                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                clickPos = event.pos
                                if 13 < clickPos[0] < 261 and 663 < clickPos[1] < 760:
                                    tutorialCheck = 1
                                    ammo = 100
                                    reload_time = 2.5
                                    reloading = False
                                    outOfAmmo = False
                                    lastReloadTime = 0
                    tutorialCheck = 0

                if 18 < clickPos[0] < 255 and 155 < clickPos[1] < 582:
                    while retry:
                        levelNum = Level(screen, level)
                        KillNeededNum = KillsNeeded(screen, (5 + (5 * level)) - killCount)
                        lives = Life(screen, origionalHearts - death_count)

                        clock.tick(frame_rate)

                        controller.get_and_handle_events()
                        game.run_one_cycle()
                        viewer.draw_everything()
                        count = count + 1

                        EasySpawnTimer = EasySpawnTimer + 1
                        MediumSpawnTimer = MediumSpawnTimer + 1
                        HardSpawnTimer = HardSpawnTimer + 1

                        if EasySpawnTimer == 54 - (4 * level):
                            EasySpawnTimer = 0
                            spawn.enemies()

                        if MediumSpawnTimer == 105 - (5 * level):
                            MediumSpawnTimer = 0
                            spawn.MediumEnemies()

                        if HardSpawnTimer == 205 - (5 * level):
                            HardSpawnTimer = 0
                            spawn.HardEnemies()

                        pressed_keys = pygame.key.get_pressed()
                        if pressed_keys[pygame.K_LEFT] and game.player.x + game.player.image.get_width() / 2 > 0:
                            game.player.x -= 20
                        if pressed_keys[pygame.K_RIGHT] and game.player.x < \
                                game.screen.get_width() - game.player.image.get_width() / 2:
                            game.player.x += 20
                        if pressed_keys[pygame.K_UP] and game.player.y > 0:
                            game.player.y -= 20
                        if pressed_keys[pygame.K_DOWN] and game.player.y < \
                                game.screen.get_height() - game.player.image.get_height() * (3 / 4):
                            game.player.y += 20
                        if pressed_keys[pygame.K_ESCAPE]:
                            sys.exit()

                        if reloading and time.time() - lastReloadTime > reload_time:
                            reloading = False
                            game.ammo.ammo = 100
                        if reloading is False and pressed_keys[pygame.K_SPACE] and ammo > 0:
                            ammo -= 1
                            game.player.fire()
                            game.ammo.ammo -= 1
                        if pressed_keys[pygame.K_RSHIFT] or pressed_keys[pygame.K_LSHIFT] or ammo == 0:
                            lastReloadTime = time.time()
                            reloading = True
                            ammo = full_ammo

                        for spawnPoint in spawn.spawnPoint:
                            for lasers in game.player.lasers:
                                if spawnPoint.hit_by(lasers):
                                    spawnPoint.life -= 1
                                    lasers.has_exploded = True
                                    if spawnPoint.life == 0:
                                        spawnPoint.is_dead = True
                                        killCount = killCount + 1

                        for spawnPoint in spawn.spawnPoint:
                            if game.player.hit_by(spawnPoint):
                                spawnPoint.is_dead = True
                                death_count += 1

                        bg.update()
                        bg.render()

                        for lasers in game.player.lasers:
                            lasers.move()
                            lasers.draw()

                        game.ammo.draw()
                        levelNum.draw()
                        KillNeededNum.draw()
                        lives.draw()

                        game.player.remove_exploded_lasers()

                        spawn.remove_dead_enemy()
                        spawn.draw()

                        game.player.render()
                        game.player.update(game.player.x, game.player.y)

                        if killCount == 5 + (5 * level):
                            killCount = 0
                            level = level + 1

                        if death_count == 4:
                            reloading = False
                            outOfAmmo = False
                            lastReloadTime = 0
                            death_count = 0
                            killCount = 0
                            level = 1
                            game.ammo.ammo = 100
                            for lasers in game.player.lasers:
                                lasers.has_exploded = True
                            for k in range(len(spawn.spawnPoint) - 1, -1, -1):
                                del spawn.spawnPoint[k]
                            while menu1 == True:
                                restart.render()
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        retry = True
                                        menu1 = False
                                    pressed_keys = pygame.key.get_pressed()
                                    if pressed_keys[pygame.K_BACKSPACE]:
                                        retry = False
                                        menu1 = False
                            menu1 = True

                        pygame.display.update()
        pygame.display.update()


main()
