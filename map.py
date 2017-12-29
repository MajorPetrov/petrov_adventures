#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: module

:author: Vladimir Razdobreev

:date: 2017, december


Map and camera classes for the game

Petrov_against_cosmopolitans - platform game

"""

import pygame as pg
from settings import *


class Map:
    def __init__(self, filename):
        self.data = []

        with open(filename) as data:
            for line in data:
                self.data.append(line)

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILE_SIZE
        self.height = self.tileheight * TILE_SIZE


class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - WIDTH), x)  # right
        y = max(-(self.height - HEIGHT), y)  # bottom

        self.camera = pg.Rect(x, y, self.width, self.height)
