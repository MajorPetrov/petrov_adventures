#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: module

:author: Vladimir Razdobreev

:date: 2017, december


Main game file - the main program loop

Petrov_against_cosmopolitans - platform game

"""

from os import path
from map import *
from sprites import *


class Game:
    def __init__(self):
        """
        Initialize game window
        """
        # initialize pygame and create window
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITLE)

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True

    def load_data(self):
        folder = path.dirname(__file__)
        self.map = Map(path.join(folder, "level_1"))

    def new(self):
        """
        Start a new game
        :return: None
        """
        self.load_data()

        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()

        self.player = Player(self, 10, 10)  # parameter self make a link between the game itself and the player
        self.all_sprites.add(self.player)

        # for platform in PLATFORM_LIST:
        #     p = Platform(*platform)  # same as platform[0], platform[1], platform[2], platform[3]
        #     self.all_sprites.add(p)
        #     self.platforms.add(p)

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    p = Platform(col, row)
                    self.all_sprites.add(p)
                    self.platforms.add(p)

        self.run()

    def run(self):
        """
        Game loop
        :return: None
        """
        while self.playing:

            # keep loop running at the right speed
            self.clock.tick(FPS)

            self.events()
            self.update()
            self.draw()

    def update(self):
        """
        Game loop - update (collision check)
        :return: None
        """
        self.all_sprites.update()

        # check if the player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)

            if hits:
                self.player.pos.y = hits[0].rect.top + 2
                self.player.vel.y = 0

        # if player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)  # velocity is negative when jumping

            # taking all platforms
            for platform in self.platforms:
                platform.rect.y += abs(self.player.vel.y)  # platform will move in the same time as the player

        if self.player.rect.bottom >= HEIGHT * 3 / 4:
            self.player.pos.y -= self.player.vel.y

            for platform in self.platforms:
                platform.rect.y -= self.player.vel.y

    def events(self):
        """
        Game loop - Process input (events)
        :return: None
        """
        for event in pg.event.get():

            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False

                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        """
        Game loop - draw / render
        :return: None
        """
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        # after drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        """
        Game splash / start screen
        :return: None
        """
        pass

    def show_go_screen(self):
        """
        Game over / continue screen
        :return: None
        """
        pass


g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
