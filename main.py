#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: module

:author: Vladimir Razdobreev

:date: 2017, december


Main game file - the main program loop

Petrov_against_cosmopolitans - platform game

"""

import pygame as pg
from settings import *


class Game:
    def __init__(self):
        """
        Initialize game window
        """
        # initialize pygame and create window
        self.playing = True
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITLE)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        """
        Start a new game
        :return: None
        """
        self.all_sprites = pg.sprite.Group()
        g.run()

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
        Game loop - update
        :return: None
        """
        self.all_sprites.update()

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
