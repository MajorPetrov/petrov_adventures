#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: module

:author: Vladimir Razdobreev

:date: 2017, december


Sprite classes for Petrov_against_cosmopolitans - platform game

"""

import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0

    def update(self):
        self.vx = 0
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.vx = -5

        if keys[pg.K_RIGHT]:
            self.vx = 5

        self.rect.x += self.vx
        self.rect.y += self.vy
