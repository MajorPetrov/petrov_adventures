#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: module

:author: Vladimir Razdobreev

:date: 2017, december


Sprite classes for the game

Petrov_against_cosmopolitans - platform game

"""

import pygame as pg
from settings import *

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)

        self.game = game

        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

        self.pos = vec(x * TILE_SIZE, y * TILE_SIZE)  # position vector
        self.vel = vec(0, 0)  # velocity vector
        self.acc = vec(0, 0)  # acceleration vector

    def update(self):
        self.collision()

        self.acc = vec(0, PLAYER_GRAV)  # gravity acceleration
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC

        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION

        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + PLAYER_ACC * self.acc

        # wrap around the sides of the screen
        # if self.pos.x > WIDTH:
        #     self.pos.x = 0
        #
        # if self.pos.x < 0:
        #     self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def collision(self):
        # for wall in self.game.all_sprites:
        #     if wall.left == self.rect.right:
        #         self.acc = vec(0, 0)
        #         self.vel = vec(0, 0)
        #
        #     elif wall.right == self.rect.left:
        #         self.acc = vec(0, 0)
        #         self.vel = vec(0, 0)

        # check if the player hits a platform - only if falling
        if self.vel.y > 0:
            hits = pg.sprite.spritecollide(self, self.game.platforms, False)

            if hits:
                self.pos.y = hits[0].rect.top + 2
                self.vel.y = 0

    def jump(self):
        # the player can jump only if he's standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1

        if hits:
            self.vel.y = -15


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
